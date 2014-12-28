from django.db import models
from .recipe import Recipe

class Direction(models.Model):
    filename = 'DIRECTION'
    
    Recipe    = models.ForeignKey(Recipe)
    StepNumber  = models.IntegerField(null=True, blank=True)
    Description = models.TextField(null=True, blank=True)


    def __unicode__(self):
        return u"%s. %s" % (self.StepNumber, self.Description[:80])