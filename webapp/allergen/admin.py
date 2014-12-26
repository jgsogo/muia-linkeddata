from django.contrib import admin
from allergen.models import *

class AllergenAdmin(admin.ModelAdmin):
    list_display = ['Group', 'Type', 'Common']

admin.site.register(Allergen, AllergenAdmin)

