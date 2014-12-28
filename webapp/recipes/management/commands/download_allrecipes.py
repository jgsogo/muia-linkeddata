#!/usr/bin/env python
# encoding: utf-8

import os
import time
import chardet
import codecs
import json
import random
import string

from optparse import make_option
from fractions import Fraction
from isodate import parse_duration
import urlparse

from django.core.management.base import BaseCommand, CommandError
from django.core import serializers
from utils.apiscraper import APIScraper
from recipes.models import Recipe, Ingredient, IngredientWithAmount, Direction


class Command(BaseCommand):
    help = u"Download some recipes from http://allrecipes.com to local file (json)"
    option_list = BaseCommand.option_list + (
        make_option('--max',
            action='store',
            dest='max',
            default=100,
            help='Max number of recipes to save'),
        make_option('--filename',
            action='store',
            dest='filename',
            default= 'recipes.json',
            help='Filename to store data to. Defaults to "recipes.json"'),
        make_option('--foods',
            action='store_true',
            default=False,
            dest='create_foods',
            help='Create foods from ingredient names',
            ),
        )
    scraper = APIScraper()
    create_foods = False

    def ingredient_NDB_No_generator(self, id_size=5, chars=string.ascii_uppercase + string.digits):
        id_size = id_size -1 # 'x' char will be prepended
        c = ''.join(random.choice(chars) for _ in range(id_size))
        while Ingredient.objects.filter(NDB_No='x'+c).exists():
            c = ''.join(random.choice(chars) for _ in range(id_size))
        return 'x'+c

    def handle_ingredient(self, recipe, name, amount, ingredientid, grams):
        self.stdout.write(u"\t - ingredient: %s | %s" % (amount, name))
        # Look for food
        ingredient = Ingredient.objects.search(name)
        if not ingredient:
            if self.create_foods:
                ingredient = Ingredient()
                ingredient.NDB_No = self.ingredient_NDB_No_generator();
                ingredient.Shrt_Desc = name
                ingredient.Long_Desc = name
                ingredient.save()
            else:
                raise Exception("Ingredient failed!")
        ing_amount = IngredientWithAmount(Recipe=recipe, Ingredient=ingredient)
        ing_amount.HumanReadable = u"%s %s" % (amount, name)
        ing_amount.GramsEquiv = grams
        # Quantity and Units
        items = amount.split()
        try:
            ing_amount.Quantity = float(sum(Fraction(part) for part in items[0].split()))
            ing_amount.Units = items[-1]
            self.stdout.write(u"\t   + ingredient: %s" % (ingredient.Shrt_Desc))
            self.stdout.write(u"\t   + quantity: %s" % (ing_amount.Quantity))
            self.stdout.write(u"\t   + units: %s" % (ing_amount.Units))
            ing_amount.save()
        except Exception as e:
            self.stderr.write(str(e))
            ingredient.delete()
            raise Exception("Quanty and units not parseable: %r" % amount)

    def handle_recipe(self, data, url):
        if Recipe.objects.filter(URL=url).exists():
            self.stdout.write(u"\t   already in database")
            return 1, False 

        recipe = Recipe(Title=data[u"name"], URL=url)
        self.stdout.write(u"\t - author: %s" % data.get(u"author", None))
        recipe.Author = data.get(u"author", None)
        self.stdout.write(u"\t - image: %s" % data.get(u"image", None))
        recipe.Image = data.get(u"image", None)
        self.stdout.write(u"\t - ratingValue: %s" % data.get(u"ratingValue", None))
        recipe.Rating = data.get(u"ratingValue", None)
        self.stdout.write(u"\t - description: %s" % data.get(u"description", '')[:60])
        recipe.Description = data.get(u"description", None)


        # Produces
        self.stdout.write(u"\t - Produces: %s" % data[u"name"])
        ingredient = Ingredient.objects.search(data[u"name"])
        if not ingredient:
            if self.create_foods:
                ingredient = Ingredient()
                ingredient.NDB_No = self.ingredient_NDB_No_generator();
                ingredient.Shrt_Desc = data[u"name"]
                ingredient.Long_Desc = data[u"name"]
                ingredient.save()
            else:
                return None, False
        recipe.Produces = ingredient

        # Yields
        self.stdout.write(u"\t - yields: %s" % data.get(u"yields", None))
        yields = data.get(u"yields", None)
        if yields:
            items = [it for it in yields.split() if it.isdigit()]
            if items:
                recipe.Yields = items[0]
            self.stdout.write(u"\t   + yields: %s -> %s" % (yields, recipe.Yields))

        # PrepTime and CookTime
        def minutes(value_str):
            if value_str:
                t = parse_duration(value_str)
                return int(t.seconds/60.)
            return None
        self.stdout.write(u"\t - prepTime: %s" % minutes(data.get(u"prepTime", None)))
        self.stdout.write(u"\t - cookTime: %s" % minutes(data.get(u"cookTime", None)))
        recipe.PrepTime = minutes(data.get(u"prepTime", None))
        recipe.CookTime = minutes(data.get(u"cookTime", None))

        recipe.save()

        # Ingredients
        try:
            for name, amount, ingredientid, grams in zip(data[u"ingredients-name"], data[u"ingredients-amount"], data["ingredients-data-ingredientid"], data[u"ingredients-data-grams"]):
                self.handle_ingredient(recipe, name, amount, ingredientid, grams)
        except Exception as e:
            self.stderr.write(str(e))
            recipe.delete() # Al borrar el recipe, se borran todos los relacionados (IngredientWithAmount) para no quedar huérfanos
            return None, False

        #Directions
        try:
            i = 1
            self.stdout.write(u"\t - directions:")
            for direction in data.get(u"directions"):
                d = Direction(Recipe=recipe, StepNumber=i)
                d.Description = direction
                d.save()
                self.stdout.write(u"\t   + %s" % d)
                i += 1
        except Exception as e:
            self.stderr.write(str(e))
            recipe.delete() # Al borrar el recipe, se borran todos los relacionados (IngredientWithAmount) para no quedar huérfanos
            return None, False

        return recipe, True

    def handle(self, *args, **options):
        #import pdb; pdb.set_trace()
        max_recipes = int(options['max'])
        filename = options['filename']
        self.create_foods = options['create_foods']

        t1 = time.time()

        n_recipes = 0
        errors = 0
        i = 0
        next = "http://allrecipes.com/recipes/main.aspx?Page=1"

        to_print = []
        while n_recipes < max_recipes:
            # Call index
            self.stdout.write("Calling next index page %r" % next)
            data = self.scraper.scrape_url(next)
            next = data['next']
            for url in data['recipes']:
                full_url = urlparse.urljoin('http://allrecipes.com/', url)
                #try:
                self.stdout.write("\n\t%s/%s" % (i+1, max_recipes), ending='')
                recipe_data = self.scraper.scrape_url(full_url)
                self.stdout.write(" %s" % (recipe_data[u'name']))

                recipe, append = self.handle_recipe(recipe_data, full_url)
                if recipe:
                    n_recipes += 1
                    if append:
                        to_print.append(recipe)
                else:
                    errors += 1
                
                i += 1
                if i >= max_recipes:
                    break
                #except Exception as e:
                #    self.stderr(e)

        with open(filename, "w") as out:
            serializers.serialize('json', to_print, indent=4, stream=out)

        t2 = time.time()
        self.stdout.write(u"Retrieved %r recipes of %r tried (%s errors)" % (n_recipes, max_recipes, errors))
        self.stdout.write('Exec time: ' + str(round(t2 - t1)))

