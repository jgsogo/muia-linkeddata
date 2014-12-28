
from django.db import models

from food.models import Food
from .disease import Disease

class FoodCausesDiseaseManager(models.Manager):

    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = Food.objects.get(NDB_No = list[0])
        instance.DiseaseName =  Disease.objects.get(DiseaseName = list[1])
        instance.save()
        return instance

class FoodCausesDisease(models.Model):
    filename = 'FOODCAUSES'

    NDB_No      = models.ForeignKey(Food)
    DiseaseName = models.ForeignKey(Disease)

    objects = FoodCausesDiseaseManager()

    