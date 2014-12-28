from django.db import models

class Direction(models.Model):
    filename = 'DIRECTION'

    Direction   = models.CharField(max_length=255, primary_key=True)
    Description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title