# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0017_vdnserver_last_response_datasets'),
    ]

    operations = [
        migrations.AddField(
            model_name='vdndataset',
            name='url',
            field=models.TextField(default=''),
        ),
    ]
