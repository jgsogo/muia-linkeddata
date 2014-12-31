from django.contrib import admin
from diseases.models import *

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['DiseaseName', 'DOID']

class FoodCausesDiseaseAdmin(admin.ModelAdmin):
    list_display = ['NDB_No', 'DiseaseKey']

class NutrientCausesDiseaseAdmin(admin.ModelAdmin):
    list_display = ['NutrientID', 'DiseaseKey']

class AllergenCausesDiseaseAdmin(admin.ModelAdmin):
    list_display = ['GI_No', 'DiseaseKey']

admin.site.register(Disease, DiseaseAdmin)
admin.site.register(FoodCausesDisease, FoodCausesDiseaseAdmin)
admin.site.register(NutrientCausesDisease, NutrientCausesDiseaseAdmin)
admin.site.register(AllergenCausesDisease, AllergenCausesDiseaseAdmin)

