from django.db import models

class AllergenManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.GI_No = list[0]
        instance.Group = list[1]
        instance.Main = list[2]
        instance.Type = list[3]
        instance.Species = list[4]
        instance.Common = list[5]
        instance.IUIS = list[6]
        instance.save()
        return instance

class Allergen(models.Model):
    filename = 'ALLERGEN'

    GI_No   = models.CharField(max_length=15, primary_key=True)
    Group   = models.CharField(max_length=100)
    Main    = models.CharField(max_length=10, choices=(('Non Food', 'Non Food Allergen'), ('Food','Food Allergen')))
    Type    = models.CharField(max_length=100)
    Species = models.CharField(max_length=100)
    Common  = models.CharField(max_length=100)
    IUIS    = models.CharField(max_length=25)

    objects = AllergenManager()

    def __unicode__(self):
        return u"%s, Allergy: %s" % (self.Group, self.Common)