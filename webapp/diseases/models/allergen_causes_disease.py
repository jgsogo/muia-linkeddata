
from django.db import models

from allergen.models import Allergen
from .disease import Disease

class AllergenCausesDiseaseManager(models.Manager):

    def create_from_list(self, list):
        instance = self.model()
        instance.GI_No = Allergen.objects.get(GI_No = list[0])
        instance.DiseaseKey = Disease.objects.get(DiseaseKey = list[1])
        instance.save()
        return instance

class AllergenCausesDisease(models.Model):
    filename = 'ALLECAUSES'

    GI_No      = models.ForeignKey(Allergen)
    DiseaseKey = models.ForeignKey(Disease)

    objects = AllergenCausesDiseaseManager()

    