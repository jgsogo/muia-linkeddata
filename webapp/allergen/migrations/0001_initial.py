# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('GI_No', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('Group', models.CharField(max_length=100)),
                ('Main', models.CharField(max_length=10, choices=[(b'Non Food', b'Non Food Allergen'), (b'Food', b'Food Allergen')])),
                ('Type', models.CharField(max_length=100)),
                ('Species', models.CharField(max_length=100)),
                ('Common', models.CharField(max_length=100)),
                ('IUIS', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
