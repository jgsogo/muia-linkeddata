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
                ('Group', models.CharField(max_length=100, serialize=False, primary_key=True)),
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
