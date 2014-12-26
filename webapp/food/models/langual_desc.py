from django.db import models

class LangualDescManager(models.Manager):

    def create_from_list(self, list):
        instance = self.model()
        instance.Factor_Code = list[0]
        instance.Description = list[1]
        instance.save()
        return instance

class LangualDesc(models.Model):
    filename = 'LANGDESC'

    Factor_Code = models.CharField(max_length=5, primary_key=True)
    Description = models.CharField(max_length=140)
    
    objects = LangualDescManager()

