#!/usr/bin/env python
# encoding: utf-8

import os
import time
import chardet
import codecs
import json

from optparse import make_option
import urlparse

from django.core.management.base import BaseCommand, CommandError
from django.core import serializers
from utils.apiscraper import APIScraper


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
        )
    scraper = APIScraper()

    recipes = []

    def handle_recipe(self, url):
        data = self.scraper.scrape_url(url)
        recipe_data = { 'name': data[u'name'],
                        'url': url,
                        }
        return recipe_data


    def handle(self, *args, **options):
        max_recipes = int(options['max'])
        filename = options['filename']

        t1 = time.time()

        n_recipes = 0
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
                self.stdout.write("\t%s/%s" % (n_recipes, max_recipes), ending='')
                recipe_data = self.handle_recipe(full_url)
                self.stdout.write(" %s" % (recipe_data[u'name']))
                to_print.append(recipe_data)
                n_recipes += 1
                if n_recipes >= max_recipes:
                    break
                #except Exception as e:
                #    self.stderr(e)

        with open(filename, "w") as out:
            out.write(json.dumps(to_print, indent=4))

        t2 = time.time()
        self.stdout.write('Exec time: ' + str(round(t2 - t1)), 1)

