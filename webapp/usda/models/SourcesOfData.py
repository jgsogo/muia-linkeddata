#!/usr/bin/env python
# encoding: utf-8

from django.db import models

class SourcesOfDataManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.DataSrc_ID = list[0]
        instance.Authors = list[1]
        instance.Title = list[2]
        instance.Year = list[3]
        instance.Journal = list[4]
        instance.Vol_City = list[5]
        instance.Issue_State = list[6]
        instance.Start_Page = list[7]
        instance.End_Page = list[8]
        instance.save()
        return instance

class SourcesOfData(models.Model):
    filename = 'DATA_SRC'

    DataSrc_ID = models.CharField(max_length=6, primary_key=True)
    Authors = models.CharField(max_length=255, blank=True, null=True)
    Title = models.CharField(max_length=255, blank=True, null=True)
    Year = models.CharField(max_length=4, blank=True, null=True)
    Journal = models.CharField(max_length=135, blank=True, null=True)
    Vol_City = models.CharField(max_length=16, blank=True, null=True)
    Issue_State = models.CharField(max_length=5, blank=True, null=True)
    Start_Page = models.CharField(max_length=5, blank=True, null=True)
    End_Page = models.CharField(max_length=5, blank=True, null=True)

    objects = SourcesOfDataManager()

    class Meta:
        app_label = 'usda'
