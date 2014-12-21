#!/usr/bin/env python
# encoding: utf-8

from django.db import models

class FoodGroupManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.FdGrp_cd = list[0]
        instance.FdGrp_Desc = list[1]
        instance.save()
        return instance

class FoodGroup(models.Model):
    filename = 'FD_GROUP'

    FdGrp_cd = models.CharField(max_length=4, primary_key=True)
    FdGrp_Desc = models.CharField(max_length=60)

    object = FoodGroupManager()
    class Meta:
        app_label = 'usda'