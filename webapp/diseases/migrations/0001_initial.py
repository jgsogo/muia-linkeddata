# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('Disease', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('Description', models.TextField(null=True, blank=True)),
                ('Food', models.CharField(max_length=100)),
                ('Nutrient', models.CharField(max_length=100)),
                ('Allergen', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
