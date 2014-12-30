#!/usr/bin/env python
# encoding: utf-8

from django.db import models

from .food import Food
from .langual_desc import LangualDesc

class LangualManager(models.Manager):

    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = Food.objects.get(NDB_No = list[0])
        instance.Factor_Code = LangualDesc.objects.get(Factor_Code = list[1])
        instance.save()
        return instance

class Langual(models.Model):
    filename = 'LANGUAL'

    NDB_No      = models.ForeignKey(Food) #! TODO: Esto debería ser 'primary_key', pero entonces hay que cambiarlo en muchos más sitios (NO CORREGIR)
    Factor_Code = models.ForeignKey(LangualDesc)
    
    objects = LangualManager()

    def __unicode__(self):
        return u"%s, %s" % (self.NDB_No, self.Factor_Code)