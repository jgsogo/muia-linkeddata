#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from .FoodGroup import FoodGroup

class FoodDescriptionManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = list[0]
        instance.FdGrp_Cd = FoodGroup.objects.get(FdGrp_Cd=list[1])
        instance.Long_Desc = list[2]
        instance.Shrt_Desc = list[3]

        instance.ComName = list[4]
        instance.ManufacName = list[5]
        instance.Survey = list[6]
        instance.Ref_desc = list[7]
        instance.Refuse = list[8]
        instance.SciName = list[9]
        instance.N_Factor = list[10]
        instance.Pro_Factor = list[11]
        instance.Fat_Factor = list[12]
        instance.CHO_Factor = list[13]
        instance.save()
        return instance

class FoodDescription(models.Model):
    filename = 'FOOD_DES'

    NDB_No = models.CharField(max_length=5, primary_key=True)
    FdGrp_Cd = models.ForeignKey(FoodGroup)
    Long_Desc = models.CharField(max_length=200)
    Shrt_Desc = models.CharField(max_length=60)

    ComName = models.CharField(max_length=100, blank=True, null=True)
    ManufacName = models.CharField(max_length=65, blank=True, null=True)
    Survey = models.BooleanField(default=False)
    Ref_desc = models.CharField(max_length=135, blank=True, null=True)
    Refuse = models.IntegerField(blank=True, null=True)
    SciName = models.CharField(max_length=65, blank=True, null=True)
    N_Factor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Pro_Factor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Fat_Factor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    CHO_Factor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    objects = FoodDescriptionManager()
    class Meta:
        app_label = 'usda'