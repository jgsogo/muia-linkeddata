#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from .NutrientDefinition import NutrientDefinition
from .SourceCode import SourceCode
from .DataDerivationCode import DataDerivationCode


class NutrientDataManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = list[0]
        instance.Nutr_No = NutrientDefinition.objects.get(Nutr_No=list[1])
        instance.Nutr_Val = list[2]
        instance.Num_Data_Pts = list[3]
        instance.Std_Error = list[4]
        instance.Src_Cd = SourceCode.objects.get(Src_Cd=list[5])
        if list[6]:
            instance.Deriv_Cd = DataDerivationCode.objects.get(Deriv_Cd=list[6])
        instance.Ref_NDB_No = list[7]
        instance.Add_Nutr_Mark = list[8]
        instance.Num_Studies = list[9]
        instance.Min = list[10]
        instance.Max = list[11]
        instance.DF = list[12]
        instance.Low_EB = list[13]
        instance.Up_EB = list[14]
        instance.Stat_cmt = list[15]
        instance.AddMod_Date = list[16]
        instance.CC = list[17]
        instance.save()
        return instance

class NutrientData(models.Model):
    filename = 'NUT_DATA'

    NDB_No = models.CharField(max_length=5, primary_key=True)
    Nutr_No = models.ForeignKey(NutrientDefinition)
    Nutr_Val = models.DecimalField(max_digits=13, decimal_places=3)
    Num_Data_Pts = models.DecimalField(max_digits=5, decimal_places=0)
    Std_Error = models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True)
    Src_Cd = models.ForeignKey(SourceCode)
    Deriv_Cd = models.ForeignKey(DataDerivationCode, blank=True, null=True)
    Ref_NDB_No = models.CharField(max_length=5, blank=True, null=True)
    Add_Nutr_Mark = models.CharField(max_length=1, blank=True, null=True)
    Num_Studies = models.IntegerField(blank=True, null=True)
    Min = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    Max = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    DF = models.IntegerField(blank=True, null=True)
    Low_EB = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    Up_EB = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    Stat_cmt = models.CharField(max_length=10, blank=True, null=True)
    AddMod_Date = models.DateTimeField(blank=True, null=True)
    CC = models.CharField(max_length=1, blank=True, null=True)

    objects = NutrientDataManager()

    class Meta:
        app_label = 'usda'