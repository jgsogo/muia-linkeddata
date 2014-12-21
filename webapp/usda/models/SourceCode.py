#!/usr/bin/env python
# encoding: utf-8

from django.db import models

class SourceCodeManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.Src_Cd = list[0]
        instance.SrcCd_Desc = list[1]
        instance.save()
        return instance

class SourceCode(models.Model):
    filename = 'SRC_CD'

    Src_Cd = models.CharField(max_length=2)
    SrcCd_Desc = models.CharField(max_length=60)

    objects = SourceCodeManager()

    class Meta:
        app_label = 'usda'