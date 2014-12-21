#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from .NutrientData import NutrientData

class FootnoteManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = list[0]
        instance.Footnt_No = list[1]
        instance.Footnt_Typ = list[2]
        if list[3]:
            instance.Nutr_No = NutrientData.objects.get(Nutr_No=list[3])
        instance.Footnt_Txt = list[4]
        instance.save()
        return instance

class Footnote(models.Model):
    filename = 'FOOTNOTE'

    NDB_No = models.CharField(max_length=5, primary_key=True)
    Footnt_No = models.CharField(max_length=4)
    Footnt_Typ = models.CharField(max_length=1, choices=(('D', 'Footnote to FoodDescription'), ('M','Footnote to measure description'), ('N', 'Footnote to Nutrient')))
    Nutr_No = models.ForeignKey(NutrientData, blank=True, null=True)
    Footnt_Txt = models.CharField(max_length=200)

    objects = FootnoteManager()
    class Meta:
        app_label = 'usda'