# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 09:49
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userselection',
            name='json_field',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True),
        ),
    ]