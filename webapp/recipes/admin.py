from django.contrib import admin

from recipes.models import *

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['Title']

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['NDB_No', 'Long_Desc']

class IngredientWithAmountAdmin(admin.ModelAdmin):
    list_display = ['Ingredient', 'Quantity']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientWithAmount, IngredientWithAmountAdmin)
admin.site.register(Direction)
