#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from .LangualFactorsDescription import LangualFactorsDescription

class LangualFactorManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = list[0]
        instance.Factor_Code = LangualFactorsDescription.objects.get(Factor_Code = list[1])
        instance.save()
        return instance


class LangualFactor(models.Model):
    filename = 'LANGUAL'

    NDB_No = models.CharField(max_length=5, primary_key=True)
    Factor_Code = models.ForeignKey(LangualFactorsDescription)

    objects = LangualFactorManager()

    class Meta:
        app_label = 'usda'