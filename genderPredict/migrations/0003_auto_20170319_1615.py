# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genderPredict', '0002_auto_20170319_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genderpredictions',
            name='is_predict_right',
            field=models.BooleanField(default=True),
        ),
    ]