
from django.db import models

from allergen.models import Allergen
from .disease import Disease

class AllergenCausesDiseaseManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.AllergenID = Allergen.objects.get(Group = list[0])
        instance.DiseaseName = Disease.objects.get(DiseaseName = list[1])
        instance.save()
        return instance

class AllergenCausesDisease(models.Model):
    filename = 'ALLECAUSES'

    AllergenID  = models.ForeignKey(Allergen)
    DiseaseName = models.ForeignKey(Disease)

    objects = AllergenCausesDiseaseManager()

    