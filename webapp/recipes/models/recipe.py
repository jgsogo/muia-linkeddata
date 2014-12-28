from django.db import models

from food.models import Food
from .ingredient import Ingredient


class Recipe(models.Model):

    URL         = models.URLField(null=True, blank=True)

    Title       = models.CharField(max_length=255)
    Description = models.TextField(null=True, blank=True)
    Author      = models.CharField(max_length=255, null=True, blank=True)
    CookTime   = models.IntegerField(null=True, blank=True, help_text=u"Time in minutes")
    PrepTime    = models.IntegerField(null=True, blank=True, help_text=u"Time in minutes")
    Image       = models.URLField(null=True, blank=True)
    Rating      = models.FloatField(null=True, blank=True)

    Produces    = models.ForeignKey(Food, related_name='is_produced')
    Yields      = models.IntegerField(null=True, blank=True)
    
    Ingredients = models.ManyToManyField(Ingredient, through='IngredientWithAmount')

    def __unicode__(self):
        return self.Title