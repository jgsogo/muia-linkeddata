# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='Long_Desc',
            field=models.CharField(max_length=512),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='food',
            name='Shrt_Desc',
            field=models.CharField(max_length=140),
            preserve_default=True,
        ),
    ]
