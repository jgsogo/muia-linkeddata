
from django.db import models

from food.models import Food


class Ingredient(Food):
    class Meta:
        proxy = True
    
