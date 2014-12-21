#!/usr/bin/env python
# encoding: utf-8

from django.db import models

class DataDerivationCodeManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.Deriv_Cd = list[0]
        instance.Deriv_Desc = list[1]
        instance.save()
        return instance

class DataDerivationCode(models.Model):
    filename = 'DERIV_CD'

    Deriv_Cd = models.CharField(max_length=4, primary_key=True)
    Deriv_Desc = models.CharField(max_length=120)

    objects = DataDerivationCodeManager()

    class Meta:
        app_label = 'usda'