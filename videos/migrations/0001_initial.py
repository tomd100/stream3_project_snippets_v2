# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 15:57
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
            name='SnippetItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snippet_title', models.CharField(max_length=60)),
                ('snippet_start', models.FloatField(default=0)),
                ('snippet_end', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VideoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=60)),
                ('video_url', models.URLField(max_length=60)),
                ('video_start', models.FloatField(default=0)),
                ('video_end', models.FloatField(default=0)),
                ('video_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='snippetitem',
            name='snippet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.VideoItem'),
        ),
    ]
