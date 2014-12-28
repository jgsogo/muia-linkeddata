from django.db import models
from .recipe import Recipe

class Direction(models.Model):
    
    Recipe    = models.ForeignKey(Recipe)
    StepNumber  = models.IntegerField()
    Description = models.TextField()

    def __unicode__(self):
        return u"%s. %s" % (self.StepNumber, self.Description[:40])