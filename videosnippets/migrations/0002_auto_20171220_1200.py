# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 12:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videosnippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SnippetItem',
            new_name='Snippet',
        ),
    ]
