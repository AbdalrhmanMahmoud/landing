# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-05 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_remove_page_leave_capture'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='small_heading',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]