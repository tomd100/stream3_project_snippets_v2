# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-30 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videocategory',
            name='video',
        ),
        migrations.AlterField(
            model_name='videocategory',
            name='category',
            field=models.CharField(default='General', max_length=500),
        ),
    ]