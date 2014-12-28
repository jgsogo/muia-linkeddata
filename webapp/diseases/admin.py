from django.contrib import admin
from diseases.models import *

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['Disease', 'DOID']

class FoodCausesDiseaseAdmin(admin.ModelAdmin):
    list_display = ['FoodID', 'DiseaseName']

class NutrientCausesDiseaseAdmin(admin.ModelAdmin):
    list_display = ['NutrientID', 'DiseaseName']

class AllergenCausesDiseaseAdmin(admin.ModelAdmin):
    list_display = ['AllergenID', 'DiseaseName']

admin.site.register(Disease, DiseaseAdmin)
admin.site.register(FoodCausesDisease, FoodCausesDiseaseAdmin)
admin.site.register(NutrientCausesDisease, NutrientCausesDiseaseAdmin)
admin.site.register(AllergenCausesDisease, AllergenCausesDiseaseAdmin)

