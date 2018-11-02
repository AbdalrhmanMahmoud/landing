# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-01 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20181101_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='small_heading',
            field=models.CharField(blank=True, help_text='This is the grey text', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='image_bg',
            field=models.URLField(blank=True, help_text='uplade back grond to the first part of the page ', null=True),
        ),
    ]