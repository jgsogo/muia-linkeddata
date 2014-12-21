from django.db import models

from food.models import Food

from .ingredient import Ingredient


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    produces = models.ForeignKey(Food, related_name='is_produced')
    yields = models.IntegerField(null=True, blank=True)

    ingredients = models.ManyToManyField(Ingredient, through='recipes.IngredientWithAmount')

    def __unicode__(self):
        return self.title