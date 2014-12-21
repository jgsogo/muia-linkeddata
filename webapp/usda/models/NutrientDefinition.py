#!/usr/bin/env python
# encoding: utf-8

from django.db import models

class NutrientDefinitionManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.Nutr_No = list[0]
        instance.Units = list[1]
        instance.Tagname = list[2]
        instance.NutrDesc = list[3]
        instance.Num_Dec = list[4]
        instance.SR_Order = list[5]
        instance.save()
        return instance


class NutrientDefinition(models.Model):
    filename = 'NUTR_DEF'

    Nutr_No = models.CharField(max_length=3, primary_key=True)
    Units = models.CharField(max_length=7)
    Tagname = models.CharField(max_length=20, blank=True, null=True)
    NutrDesc = models.CharField(max_length=60)
    Num_Dec = models.IntegerField()
    SR_Order = models.IntegerField()

    objects = NutrientDefinitionManager()

    class Meta:
        app_label = 'usda'