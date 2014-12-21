# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataDerivationCode',
            fields=[
                ('Deriv_Cd', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('Deriv_Desc', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSourceLink',
            fields=[
                ('NDB_No', models.CharField(max_length=5, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodDescription',
            fields=[
                ('NDB_No', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('Long_Desc', models.CharField(max_length=200)),
                ('Shrt_Desc', models.CharField(max_length=60)),
                ('ComName', models.CharField(max_length=100, null=True, blank=True)),
                ('ManufacName', models.CharField(max_length=65, null=True, blank=True)),
                ('Survey', models.BooleanField(default=False)),
                ('Ref_desc', models.CharField(max_length=135, null=True, blank=True)),
                ('Refuse', models.IntegerField(null=True, blank=True)),
                ('SciName', models.CharField(max_length=65, null=True, blank=True)),
                ('N_Factor', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('Pro_Factor', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('Fat_Factor', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('CHO_Factor', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('FdGrp_cd', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('FdGrp_Desc', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Footnote',
            fields=[
                ('NDB_No', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('Footnt_No', models.CharField(max_length=4)),
                ('Footnt_Typ', models.CharField(max_length=1, choices=[(b'D', b'Footnote to FoodDescription'), (b'M', b'Footnote to measure description'), (b'N', b'Footnote to Nutrient')])),
                ('Footnt_Txt', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LangualFactor',
            fields=[
                ('NDB_No', models.CharField(max_length=5, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LangualFactorsDescription',
            fields=[
                ('Factor_Code', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('Description', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NutrientData',
            fields=[
                ('NDB_No', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('Nutr_Val', models.DecimalField(max_digits=13, decimal_places=3)),
                ('Num_Data_Pts', models.DecimalField(max_digits=5, decimal_places=0)),
                ('Std_Error', models.DecimalField(null=True, max_digits=11, decimal_places=3, blank=True)),
                ('Ref_NDB_No', models.CharField(max_length=5, null=True, blank=True)),
                ('Add_Nutr_Mark', models.CharField(max_length=1, null=True, blank=True)),
                ('Num_Studies', models.IntegerField(null=True, blank=True)),
                ('Min', models.DecimalField(null=True, max_digits=13, decimal_places=3, blank=True)),
                ('Max', models.DecimalField(null=True, max_digits=13, decimal_places=3, blank=True)),
                ('DF', models.IntegerField(null=True, blank=True)),
                ('Low_EB', models.DecimalField(null=True, max_digits=13, decimal_places=3, blank=True)),
                ('Up_EB', models.DecimalField(null=True, max_digits=13, decimal_places=3, blank=True)),
                ('Stat_cmt', models.CharField(max_length=10, null=True, blank=True)),
                ('AddMod_Date', models.DateTimeField(null=True, blank=True)),
                ('CC', models.CharField(max_length=1, null=True, blank=True)),
                ('Deriv_Cd', models.ForeignKey(blank=True, to='usda.DataDerivationCode', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NutrientDefinition',
            fields=[
                ('Nutr_No', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('Units', models.CharField(max_length=7)),
                ('Tagname', models.CharField(max_length=20, null=True, blank=True)),
                ('NutrDesc', models.CharField(max_length=60)),
                ('Num_Dec', models.IntegerField()),
                ('SR_Order', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SourceCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Src_Cd', models.CharField(max_length=2)),
                ('SrcCd_Desc', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SourcesOfData',
            fields=[
                ('DataSrc_ID', models.CharField(max_length=6, serialize=False, primary_key=True)),
                ('Authors', models.CharField(max_length=255, null=True, blank=True)),
                ('Title', models.CharField(max_length=255, null=True, blank=True)),
                ('Year', models.CharField(max_length=4, null=True, blank=True)),
                ('Journal', models.CharField(max_length=135, null=True, blank=True)),
                ('Vol_City', models.CharField(max_length=16, null=True, blank=True)),
                ('Issue_State', models.CharField(max_length=5, null=True, blank=True)),
                ('Start_Page', models.CharField(max_length=5, null=True, blank=True)),
                ('End_Page', models.CharField(max_length=5, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('NDB_No', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('Seq', models.CharField(max_length=2)),
                ('Amount', models.DecimalField(max_digits=8, decimal_places=3)),
                ('Msre_Desc', models.CharField(max_length=84)),
                ('Gm_Wgt', models.DecimalField(max_digits=8, decimal_places=1)),
                ('Num_Data_Pts', models.IntegerField(null=True, blank=True)),
                ('Std_Dev', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='nutrientdata',
            name='Nutr_No',
            field=models.ForeignKey(to='usda.NutrientDefinition'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nutrientdata',
            name='Src_Cd',
            field=models.ForeignKey(to='usda.SourceCode'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='langualfactor',
            name='Factor_Code',
            field=models.ForeignKey(to='usda.LangualFactorsDescription'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='footnote',
            name='Nutr_No',
            field=models.ForeignKey(blank=True, to='usda.NutrientData', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fooddescription',
            name='FdGrp_Cd',
            field=models.ForeignKey(to='usda.FoodGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datasourcelink',
            name='DataSrc_ID',
            field=models.ForeignKey(to='usda.SourcesOfData'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datasourcelink',
            name='Nutr_No',
            field=models.ForeignKey(to='usda.NutrientDefinition'),
            preserve_default=True,
        ),
    ]
