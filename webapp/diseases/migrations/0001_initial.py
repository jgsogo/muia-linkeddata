# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllergenCausesDisease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
    ]
