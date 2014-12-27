from django.db import models
from .food import Food
from nutrients.models import Nutrient

class FoodNutrientsManager(models.Manager):

    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = Food.objects.get(NDB_No=list[0])
        instance.Nutr_No = Nutrient.objects.get(Nutr_No=list[1])
        instance.Nutr_Val = list[2]
        instance.save()
        return instance

class FoodNutrients(models.Model):
    filename = 'NUT_FACT'

    id = models.AutoField(primary_key=True)
    NDB_No   = models.ForeignKey(Food)
    Nutr_No  = models.ForeignKey(Nutrient)
    Nutr_Val = models.DecimalField(max_digits=13, decimal_places=3)
    
    objects = FoodNutrientsManager()

    def __unicode__(self):
        return u"%s, %s" % (self.NDB_No, self.Nutr_No)