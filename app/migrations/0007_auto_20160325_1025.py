# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160325_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userselection',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
