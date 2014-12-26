from django.db import models

class FoodGroupManager(models.Model):

    def create_from_list(self, list):
        instance = self.model()
        instance.FdGrp_Cd = list[0]
        instance.FdGrp_Desc = list[1]
        instance.save()
        return instance

class FoodGroup(models.Model):
    filename = 'FOOD_GROUP'

    FdGrp_Cd   = models.CharField(max_length=4, primary_key=True)
    FdGrp_Desc = models.CharField(max_length=60)
    
    objects = FoodGroupManager()

    def __unicode__(self):
        return self.FdGrp_Desc
    
