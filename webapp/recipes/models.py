from django.db import models

from food.models import Food


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = mdoels.TextField(null=True, blank=True)

    produces = models.ForeignKey(Food)
    yields = models.IntegerField(null=True, blank=True)


    def __unicode__(self):
        return self.title