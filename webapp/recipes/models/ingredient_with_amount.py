
from django.db import models

from .ingredient import Ingredient
from .recipe import Recipe


class IngredientWithAmount(models.Model):
    Recipe      = models.ForeignKey(Recipe)
    Ingredient  = models.ForeignKey(Ingredient)
    Quantity    = models.FloatField(blank=True, null=True)
    Units       = models.CharField(blank=True, null=True, max_length=7)
    GramsEquiv  = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return u"%s %s" % (self.quantity, self.ingredient)


    