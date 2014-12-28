# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20141228_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='Description',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='direction',
            name='StepNumber',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
