# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 21:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_desc',
            field=models.CharField(default=datetime.datetime(2016, 3, 14, 21, 57, 30, 603505, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
