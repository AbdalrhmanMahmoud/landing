# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-04 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, default='page-slug'),
        ),
    ]
