from django.db import models

from food.models import Food
from .ingredient import Ingredient

class RecipeManager(models.Manager):

    def create_from_list(self, list):
        instance = self.model()
        instance.Title = list[0]
        instance.Description = list[1]
        instance.Author = list[2]
        instance.TotalTime = list[3]
        instance.Produces = list[4]
        instance.Yields = list[5]
        instance.save()
        return instance

class Recipe(models.Model):
    filename = 'RECIPE'

    Title       = models.CharField(max_length=255, primary_key=True)
    Description = models.TextField(null=True, blank=True)
    Author      = models.CharField(max_length=255)
    TotalTime   = models.IntegerField(null=True, blank=True, help_text=u"Time in minutes")
    CookTime    = models.IntegerField(null=True, blank=True, help_text=u"Time in minutes")

    Produces    = models.ForeignKey(Food, related_name='is_produced')
    Yields      = models.IntegerField(null=True, blank=True)
    
    Ingredients = models.ManyToManyField(Ingredient, through='IngredientWithAmount')

    def __unicode__(self):
        return self.title