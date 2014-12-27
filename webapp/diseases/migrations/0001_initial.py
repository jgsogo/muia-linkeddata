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
            name='Disease',
            fields=[
                ('Disease', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('Description', models.TextField(null=True, blank=True)),
                ('DOID', models.CharField(max_length=15, null=True, blank=True)),
                ('Allergen', models.ForeignKey(to='allergen.Allergen')),
                ('Food', models.ForeignKey(to='food.Food')),
                ('Nutrient', models.ForeignKey(to='nutrients.Nutrient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
