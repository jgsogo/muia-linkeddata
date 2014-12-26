from django.db import models
from .food import Food
from .langual_desc import LangualDesc

class LangualManager(models.Manager):

    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = list[0]
        instance.Factor_Code = LangualDesc.objects.get(Factor_Code = list[1])
        instance.save()
        return instance

class Langual(models.Model):
    filename = 'LANGUAL'

    NDB_No = models.CharField(max_length=5, primary_key=True)
    Factor_Code = models.ForeignKey(LangualDesc)
    
    objects = LangualManager()

