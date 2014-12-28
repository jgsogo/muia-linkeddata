# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('Nutr_No', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('Description', models.CharField(max_length=60)),
                ('Type', models.CharField(max_length=25)),
                ('Main', models.CharField(max_length=15, choices=[(b'Essential', b'Essential Nutrient'), (b'Non Essential', b'Non Essential Nutrient')])),
                ('Tagname', models.CharField(max_length=20, null=True, blank=True)),
                ('Units', models.CharField(max_length=7)),
                ('Num_Dec', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
