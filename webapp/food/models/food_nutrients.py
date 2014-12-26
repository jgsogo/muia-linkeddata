from django.db import models
from nutrients.models import Nutrient

class FoodNutrientsManager(models.Manager):

    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = list[0]
        instance.Nutr_No = Nutrient.objects.get(Nutr_No=list[1])
        instance.Nutr_Val = list[2]
        instance.save()
        return instance

class FoodNutrients(models.Model):
    filename = 'NUT_FACT'

    NDB_No   = models.CharField(max_length=5, primary_key=True)
    Nutr_No  = models.ForeignKey(Nutrient)
    Nutr_Val = models.DecimalField(max_digits=13, decimal_places=3)
    
    objects = FoodNutrientsManager()

