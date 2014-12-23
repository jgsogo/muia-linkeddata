from django.db import models

class AllergenManager(models.Manager):
    def create_from_list(self, list):
        instance = self.model()
        instance.Nutr_No = list[0]
        instance.Description = list[1]
        instance.Type = list[2]
        instance.Main = list[3]
        instance.Tagname = list[4]
        instance.Units = list[5]
        instance.Num_Dec = list[6]
        instance.save()
        return instance

class Nutrient(models.Model):
    filename = 'NUTRIENT'

    Nutr_No     = models.CharField(max_length=3, primary_key=True)
    Description = models.CharField(max_length=60)
    Type        = models.CharField(max_length=25)
    Main        = models.CharField(max_length=15, choices=(('Essential', 'Essential Nutrient'), ('Non Essential','Non Essential Nutrient')))
    Tagname     = models.CharField(max_length=20, blank=True, null=True)
    Units       = models.CharField(max_length=7)
    Num_Dec     = models.IntegerField()
