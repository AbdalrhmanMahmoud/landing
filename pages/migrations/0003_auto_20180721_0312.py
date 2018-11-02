# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-21 01:12
from __future__ import unicode_literals

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180721_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='nav_color',
            field=models.CharField(default='#ffffff', max_length=7, validators=[pages.models.layout_validator]),
        ),
    ]