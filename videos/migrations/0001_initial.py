# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 14:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField(max_length=500)),
                ('yt_id', models.URLField(blank=True, max_length=500)),
                ('start', models.FloatField(default=0)),
                ('end', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
