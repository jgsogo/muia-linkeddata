
import re
from django.db import models
from collections import Counter

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

        def match_function(str, counter, delta=1):
            qs = self.filter(Long_Desc__icontains=str).values_list('NDB_No', 'Long_Desc')
            for item in qs:
                ndb_no = item[0]
                #n_desc = len(re.findall(r"[\w']+", item[1]))
                counter[ndb_no] += delta#/n_desc

        items = re.findall(r"[\w']+", name)
        n_items = len(items)        
        counter = Counter()
        for i in xrange(n_items, 0, -1):
            #print '\niteration ', i
            for j in xrange(n_items-i+1):
                str = ' '.join(items[j:j+i])
                #print "%r" % str
                match_function(str, counter, i)
            #print '\t > ', counter.most_common(10)

        if single_instance and len(counter):
            ndb_no = counter.most_common(1)[0][0]
            return self.get(NDB_No=ndb_no)
        elif not single_instance:
            ndb_no = [it[0] for it in counter.most_common(10)]
            return self.filter(NDB_No__in=ndb_no)
        return None


class Food(models.Model):
    filename = 'FOOD'

    NDB_No    = models.CharField(max_length=5, primary_key=True)
    Long_Desc = models.CharField(max_length=512)
    Shrt_Desc = models.CharField(max_length=140)
    SciName   = models.CharField(max_length=65, blank=True, null=True)
    
    objects = FoodManager()

    def __unicode__(self):
        return u"%s, %s" % (self.NDB_No, self.Long_Desc)
