# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 11:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genderPredict', '0010_auto_20170319_1809'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GenderPredictions',
            new_name='Gender',
        ),
    ]
