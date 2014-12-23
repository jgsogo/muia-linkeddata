from django.db import models

class DiseaseManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.Disease = list[0]
        instance.Description = list[1]
        instance.Food = list[2]
        instance.Nutrient = list[3]
        instance.Allergen = list[4]
        instance.save()
        return instance

class Disease(models.Model):
    filename = 'DISEASE'

    Disease     = models.CharField(max_length=255, primary_key=True)
    Description = models.TextField(null=True, blank=True)
    Food        = models.CharField(max_length=100)
    Nutrient    = models.CharField(max_length=100)
    Allergen    = models.CharField(max_length=100)

    objects = DiseaseManager()

