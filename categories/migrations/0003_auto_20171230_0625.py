# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-30 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20171230_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocategory',
            name='category',
            field=models.CharField(max_length=500),
        ),
    ]
