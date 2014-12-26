from django.contrib import admin
from diseases.models import *

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['Disease', 'DOID']

admin.site.register(Disease, DiseaseAdmin)
