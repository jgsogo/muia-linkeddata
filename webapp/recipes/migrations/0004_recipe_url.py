# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20141228_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='URL',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
