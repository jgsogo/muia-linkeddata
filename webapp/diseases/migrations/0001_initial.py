# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allergen', '0001_initial'),
        ('food', '0001_initial'),
        ('nutrients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllergenCausesDisease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AllergenID', models.ForeignKey(to='allergen.Allergen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('DiseaseName', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('Description', models.TextField(null=True, blank=True)),
                ('DOID', models.CharField(max_length=15, null=True, blank=True)),
                ('AlleCauses', models.ManyToManyField(to='allergen.Allergen', through='diseases.AllergenCausesDisease')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodCausesDisease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DiseaseName', models.ForeignKey(to='diseases.Disease')),
                ('FoodID', models.ForeignKey(to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NutrientCausesDisease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DiseaseName', models.ForeignKey(to='diseases.Disease')),
                ('NutrientID', models.ForeignKey(to='nutrients.Nutrient')),
            ],
            options={
            },
            bases=(models.Model,),
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
            name='DiseaseName',
            field=models.ForeignKey(to='diseases.Disease'),
            preserve_default=True,
        ),
    ]
