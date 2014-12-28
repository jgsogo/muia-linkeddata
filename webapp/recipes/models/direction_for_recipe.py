from django.db import models

from .direction import Direction
from .recipe import Recipe


class DirectionForRecipe(models.Model):
    DirectionID = models.ForeignKey(Direction)
    RecipeID    = models.ForeignKey(Recipe)
    StepNumber  = models.IntegerField(null=True, blank=True)
    TotalTime   = models.IntegerField(null=True, blank=True) 

    def __unicode__(self):
        return u"%s, %s" % (self.Direction, self.RecipeID)


    