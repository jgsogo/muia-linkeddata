# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientWithAmount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('yields', models.IntegerField(null=True, blank=True)),
                ('produces', models.ForeignKey(related_name='is_produced', to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ingredientwithamount',
            name='recipe',
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
            name='ingredient',
            field=models.ForeignKey(to='recipes.Ingredient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipes.Ingredient', through='recipes.IngredientWithAmount'),
            preserve_default=True,
        ),
    ]
