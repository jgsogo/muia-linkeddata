from django.contrib import admin

from food.models import *

class FoodAdmin(admin.ModelAdmin):
    list_display = ['NDB_No', 'Long_Desc']

class LangualAdmin(admin.ModelAdmin):
    list_display = ['NDB_No', 'Factor_Code']

class LangualDescAdmin(admin.ModelAdmin):
    list_display = ['Factor_Code', 'Description']

class FoodNutrientsAdmin(admin.ModelAdmin):
    list_display = ['NDB_No', 'Nutr_No', 'Nutr_Val']

class WeightAdmin(admin.ModelAdmin):
    list_display = ['NDB_No', 'Seq', 'Amount']

admin.site.register(Food, FoodAdmin)
admin.site.register(Langual, LangualAdmin)
admin.site.register(LangualDesc, LangualDescAdmin)
admin.site.register(FoodNutrients, FoodNutrientsAdmin)
admin.site.register(Weight, WeightAdmin)