
from django.db import models

from .ingredient import Ingredient
from .recipe import Recipe


class IngredientWithAmount(models.Model):
    Recipe = models.ForeignKey(Recipe)
    Ingredient = models.ForeignKey(Ingredient)
    Quantity = models.FloatField()

    def __unicode__(self):
        return u"%s %s" % (self.quantity, self.ingredient)


    