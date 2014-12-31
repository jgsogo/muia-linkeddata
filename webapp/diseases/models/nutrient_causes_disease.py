
from django.db import models

from nutrients.models import Nutrient
from .disease import Disease

class NutrientCausesDiseaseManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.NutrientID = Nutrient.objects.get(Nutr_No = list[0])
        instance.DiseaseKey = Disease.objects.get(DiseaseKey = list[1])
        instance.save()
        return instance

class NutrientCausesDisease(models.Model):
    filename = 'NUTRCAUSES'

    NutrientID  = models.ForeignKey(Nutrient)
    DiseaseKey  = models.ForeignKey(Disease)

    objects = NutrientCausesDiseaseManager()

    