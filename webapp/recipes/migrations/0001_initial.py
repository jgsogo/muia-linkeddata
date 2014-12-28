# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('Direction', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('Description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DirectionForRecipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('StepNumber', models.IntegerField(null=True, blank=True)),
                ('TotalTime', models.IntegerField(null=True, blank=True)),
                ('DirectionID', models.ForeignKey(to='recipes.Direction')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IngredientWithAmount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Quantity', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('Title', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('Description', models.TextField(null=True, blank=True)),
                ('Author', models.CharField(max_length=255)),
                ('TotalTime', models.IntegerField(null=True, blank=True)),
                ('Yields', models.IntegerField(null=True, blank=True)),
                ('Directions', models.ManyToManyField(to='recipes.Direction', through='recipes.DirectionForRecipe')),
                ('Produces', models.ForeignKey(related_name='is_produced', to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ingredientwithamount',
            name='Recipe',
            field=models.ForeignKey(to='recipes.Recipe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='directionforrecipe',
            name='RecipeID',
            field=models.ForeignKey(to='recipes.Recipe'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('food.food',),
        ),
        migrations.AddField(
            model_name='ingredientwithamount',
            name='Ingredient',
            field=models.ForeignKey(to='recipes.Ingredient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='Ingredients',
            field=models.ManyToManyField(to='recipes.Ingredient', through='recipes.IngredientWithAmount'),
            preserve_default=True,
        ),
    ]
