# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genderPredict', '0008_auto_20170319_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genderpredictions',
            name='predict_num',
            field=models.IntegerField(null=True),
        ),
    ]
