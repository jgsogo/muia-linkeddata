from django.db import models

class FoodManager(models.Manager):

    def create_from_list(self, list):
        instance = self.model()
        instance.NDB_No = list[0]
        instance.Long_Desc = list[1]
        instance.Shrt_Desc = list[2]
        instance.SciName = list[3]
        instance.save()
        return instance

    def search(self, name, single_instance=True):
        #! TODO: Look for the best candidate based on 'name'
        #   - single_instance = True ==> return just one instance (or None)
        #   - single_instance = False ==> return a list/queryset of instances (can be empty)
        if single_instance:
            try:
                return self.get(Shrt_Desc=name)
            except self.model.DoesNotExist:
                return None
        else:
            return self.filter(Shrt_Desc=name)


class Food(models.Model):
    filename = 'FOOD'

    NDB_No    = models.CharField(max_length=5, primary_key=True)
    Long_Desc = models.CharField(max_length=512)
    Shrt_Desc = models.CharField(max_length=140)
    SciName   = models.CharField(max_length=65, blank=True, null=True)
    
    objects = FoodManager()

    def __unicode__(self):
        return u"%s, %s" % (self.NDB_No, self.Long_Desc)