#!/usr/bin/env python
# encoding: utf-8

from django.db import models

class WeightManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = list[0]
        instance.Seq = list[1]
        instance.Amount = list[2]
        instance.Msre_Desc = list[3]
        instance.Gm_Wgt = list[4]
        instance.Num_Data_Pts = list[5]
        instance.Std_Dev = list[6]
        instance.save()
        return instance

class Weight(models.Model):
    filename = 'WEIGHT'

    NDB_No = models.CharField(max_length=5, primary_key=True)
    Seq = models.CharField(max_length=2)
    Amount = models.DecimalField(max_digits=8, decimal_places=3)
    Msre_Desc = models.CharField(max_length=84)
    Gm_Wgt = models.DecimalField(max_digits=8, decimal_places=1)
    Num_Data_Pts = models.IntegerField(blank=True, null=True)
    Std_Dev = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    objects = WeightManager()

    class Meta:
        app_label = 'usda'