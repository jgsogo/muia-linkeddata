# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('NDB_No', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('Long_Desc', models.CharField(max_length=200)),
                ('Shrt_Desc', models.CharField(max_length=60)),
                ('SciName', models.CharField(max_length=65, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('FdGrp_Cd', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('FdGrp_Desc', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodGroupManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NutritionFact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nutr_Val', models.DecimalField(max_digits=13, decimal_places=3)),
                ('NDB_No', models.ForeignKey(to='food.Food')),
                ('Nutr_No', models.ForeignKey(to='nutrients.Nutrient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NutritionFactManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NDB_No', models.CharField(max_length=5)),
                ('Seq', models.CharField(max_length=2)),
                ('Amount', models.DecimalField(max_digits=8, decimal_places=3)),
                ('Msre_Desc', models.CharField(max_length=84)),
                ('Gm_Wgt', models.DecimalField(max_digits=8, decimal_places=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeightManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='food',
            name='FdGrp_Cd',
            field=models.ForeignKey(to='food.FoodGroup'),
            preserve_default=True,
        ),
    ]
