from django.contrib import admin

from food.models import *

admin.site.register(Food)
admin.site.register(Langual)
admin.site.register(LangualDesc)
admin.site.register(FoodNutrients)
admin.site.register(Weight)