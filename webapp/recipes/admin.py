from django.contrib import admin

from recipes.models import *

admin.site.register(Ingredient)
admin.site.register(IngredientWithAmount)
admin.site.register(Recipe)
