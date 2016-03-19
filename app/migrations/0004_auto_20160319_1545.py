# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160315_1959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='activity_class',
            new_name='search_term',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='q1_tag_id',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='q1_tag_outcome',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='q2_tag_id',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='q2_tag_outcome',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='q3_tag_id',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='q3_tag_outcome',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='q4_tag_id',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='q4_tag_outcome',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='q5_tag_id',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='q5_tag_outcome',
        ),
        migrations.AddField(
            model_name='userselection',
            name='suggested_activity',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='app.Activity'),
            preserve_default=False,
        ),
    ]
