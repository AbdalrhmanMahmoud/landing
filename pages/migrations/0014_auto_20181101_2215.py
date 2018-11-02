# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-01 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20181101_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='head_bttn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='head_description',
            field=models.TextField(blank=True, help_text='flexple to add html code or just text ', null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_content',
            field=models.TextField(blank=True, help_text='flexple to add html code or just text ', null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='small_heading',
            field=models.CharField(blank=True, help_text='h2 in the manin page ', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='video_embed',
            field=models.TextField(blank=True, help_text='add the embaed code ', null=True),
        ),
    ]