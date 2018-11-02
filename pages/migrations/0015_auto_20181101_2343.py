# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-01 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20181101_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='nav_color',
            field=models.CharField(blank=True, default='transparent', max_length=7, null=True, validators=[pages.models.layout_validator]),
        ),
    ]
