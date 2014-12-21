
from django.db import models

from .ingredient import Ingredient
from .recipe import Recipe


class IngredientWithAmount(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.FloatField()

    def __unicode__(self):
        return u"%s %s" % (self.quantity, self.ingredient)


    