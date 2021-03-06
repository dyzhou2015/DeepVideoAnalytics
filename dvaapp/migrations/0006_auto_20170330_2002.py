# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0005_remove_annotation_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='end_frame',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='multi_frame',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='source',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='start_frame',
        ),
        migrations.AddField(
            model_name='vlabel',
            name='source',
            field=models.CharField(choices=[('UI', 'User Interface'), ('DR', 'Directory Name'), ('AG', 'Algorithm')], default='UI', max_length=2),
        ),
        migrations.AlterField(
            model_name='vlabel',
            name='label_name',
            field=models.CharField(max_length=200),
        ),
    ]
