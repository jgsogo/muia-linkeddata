# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WeightManager',
        ),
        migrations.RemoveField(
            model_name='foodnutrients',
            name='id',
        ),
        migrations.AlterField(
            model_name='foodnutrients',
            name='NDB_No',
            field=models.CharField(max_length=5, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
