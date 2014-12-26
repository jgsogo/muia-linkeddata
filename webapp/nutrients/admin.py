from django.contrib import admin

from nutrients.models import *

class NutrientAdmin(admin.ModelAdmin):
    list_display = ['Nutr_No', 'Description']
    
admin.site.register(Nutrient, NutrientAdmin)
