from django.db import models

from food.models import Food
from allergen.models import Allergen
from nutrients.models import Nutrient

class DiseaseManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.Disease = list[0]
        instance.Description = list[1]
        instance.Food = Food.objects.get(NDB_No = list[2])
        instance.Nutrient = Nutrient.objects.get(Nutr_No = list[3])
        instance.Allergen = Allergen.objects.get(Group = list[4])
        instance.save()
        return instance

class Disease(models.Model):
    filename = 'DISEASE'

    Disease     = models.CharField(max_length=255, primary_key=True)
    Description = models.TextField(null=True, blank=True)
    Food        = models.ForeignKey(Food)
    Nutrient    = models.ForeignKey(Nutrient)
    Allergen    = models.ForeignKey(Allergen)

    objects = DiseaseManager()

