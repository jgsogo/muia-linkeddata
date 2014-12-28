# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodcausesdisease',
            old_name='FoodID',
            new_name='NDB_No',
        ),
    ]
