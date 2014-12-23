from django.db import models

class AllergenManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.Group = list[0]
        instance.Main = list[1]
        instance.Type = list[2]
        instance.Species = list[3]
        instance.Common = list[4]
        instance.IUIS = list[5]
        instance.save()
        return instance

class Allergen(models.Model):
    filename = 'ALLERGEN'

    Group   = models.CharField(max_length=100, primary_key=True)
    Main    = models.CharField(max_length=10, choices=(('Non Food', 'Non Food Allergen'), ('Food','Food Allergen')))
    Type    = models.CharField(max_length=100)
    Species = models.CharField(max_length=100)
    Common  = models.CharField(max_length=100)
    IUIS    = models.CharField(max_length=25)

    objects = AllergenManager()

