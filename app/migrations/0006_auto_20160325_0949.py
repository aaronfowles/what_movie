# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_activity_places_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='userselection',
            name='no_list',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userselection',
            name='yes_list',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
