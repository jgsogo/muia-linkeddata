# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientwithamount',
            name='HumanReadable',
            field=models.CharField(max_length=512, null=True, blank=True),
            preserve_default=True,
        ),
    ]
