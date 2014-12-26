from django.db import models

class FoodManager(models.Manager):

    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = list[0]
        instance.Long_Desc = list[2]
        instance.Shrt_Desc = list[3]
        instance.SciName = list[4]
        instance.save()
        return instance

class Food(models.Model):
    filename = 'FOOD'

# Incluye los campos de FOOD_DES: 1o, 2o, 3o, 4o y 10o

    NDB_No    = models.CharField(max_length=5, primary_key=True)
    Long_Desc = models.CharField(max_length=200)
    Shrt_Desc = models.CharField(max_length=60)
    SciName   = models.CharField(max_length=65, blank=True, null=True)
    
    objects = FoodManager()

    def __unicode__(self):
        return self.Long_Desc
    
