
from django.db import models

from nutrients.models import Nutrient
from .disease import Disease

class NutrientCausesDiseaseManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.NutrientID = Nutrient.objects.get(Nutr_No = list[0])
        instance.DiseaseName = Disease.objects.get(DiseaseName = list[1])
        instance.save()
        return instance

class NutrientCausesDisease(models.Model):
    filename = 'NUTRCAUSES'

    NutrientID  = models.ForeignKey(Nutrient)
    DiseaseName = models.ForeignKey(Disease)

    objects = NutrientCausesDiseaseManager()

    