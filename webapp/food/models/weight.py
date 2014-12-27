from django.db import models
from .food import Food

class WeightManager(models.Manager):

    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = Food.objects.get(NDB_No = list[0])
        instance.Seq = list[1]
        instance.Amount = list[2]
        instance.Msre_Desc = list[3]
        instance.Gm_Wgt = list[4]
        instance.save()
        return instance

class Weight(models.Model):
    filename = 'WEIGHT'

# Incluye los campos de WEIGHT: 1o, 2o, 3o, 4o y 5o

    NDB_No    = models.ForeignKey(Food)
    Seq       = models.CharField(max_length=2)
    Amount    = Amount = models.DecimalField(max_digits=8, decimal_places=3)
    Msre_Desc = models.CharField(max_length=84)
    Gm_Wgt    = models.DecimalField(max_digits=8, decimal_places=1)
    
    objects = WeightManager()

    def __unicode__(self):
        return u"%s, %s: %s" % (self.NDB_No, self.Seq, self.Amount)