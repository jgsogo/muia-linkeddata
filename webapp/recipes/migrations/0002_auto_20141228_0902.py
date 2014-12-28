# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directionforrecipe',
            name='DirectionID',
        ),
        migrations.RemoveField(
            model_name='directionforrecipe',
            name='RecipeID',
        ),
        migrations.RemoveField(
            model_name='direction',
            name='Direction',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='Directions',
        ),
        migrations.DeleteModel(
            name='DirectionForRecipe',
        ),
        migrations.AddField(
            model_name='direction',
            name='Recipe',
            field=models.ForeignKey(default=1, to='recipes.Recipe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='direction',
            name='StepNumber',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direction',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredientwithamount',
            name='GramsEquiv',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredientwithamount',
            name='Units',
            field=models.CharField(max_length=7, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='CookTime',
            field=models.IntegerField(help_text='Time in minutes', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ingredientwithamount',
            name='Quantity',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='TotalTime',
            field=models.IntegerField(help_text='Time in minutes', null=True, blank=True),
            preserve_default=True,
        ),
    ]
