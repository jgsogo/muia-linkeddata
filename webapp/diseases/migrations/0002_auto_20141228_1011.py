# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allergen', '0001_initial'),
        ('diseases', '0001_initial'),
        ('food', '0001_initial'),
        ('nutrients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodcausesdisease',
            name='FoodID',
            field=models.ForeignKey(to='food.Food'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disease',
            name='AlleCauses',
            field=models.ManyToManyField(to='allergen.Allergen', through='diseases.AllergenCausesDisease'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disease',
            name='FoodCauses',
            field=models.ManyToManyField(to='food.Food', through='diseases.FoodCausesDisease'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disease',
            name='NutrCauses',
            field=models.ManyToManyField(to='nutrients.Nutrient', through='diseases.NutrientCausesDisease'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='allergencausesdisease',
            name='AllergenID',
            field=models.ForeignKey(to='allergen.Allergen'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='allergencausesdisease',
            name='DiseaseName',
            field=models.ForeignKey(to='diseases.Disease'),
            preserve_default=True,
        ),
    ]
