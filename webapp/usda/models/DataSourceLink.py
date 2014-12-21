#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from .NutrientDefinition import NutrientDefinition
from .SourcesOfData import SourcesOfData

class DataSourceLinkManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = list[0]
        instance.Nutr_No = NutrientDefinition.objects.get(Nutr_No=list[1])
        instance.DataSrc_ID = SourcesOfData.objects.get(DataSrc_ID=list[2])
        instance.save()
        return instance

class DataSourceLink(models.Model):
    filename = 'DATSRCLN'

    NDB_No = models.CharField(max_length=5, primary_key=True)
    Nutr_No = models.ForeignKey(NutrientDefinition)
    DataSrc_ID = models.ForeignKey(SourcesOfData)

    objects = DataSourceLinkManager()
    class Meta:
        app_label = 'usda'