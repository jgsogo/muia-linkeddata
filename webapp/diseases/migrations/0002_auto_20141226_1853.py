# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0001_initial'),
        ('food', '0001_initial'),
        ('nutrients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='Food',
            field=models.ForeignKey(to='food.Food'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disease',
            name='Nutrient',
            field=models.ForeignKey(to='nutrients.Nutrient'),
            preserve_default=True,
        ),
    ]
