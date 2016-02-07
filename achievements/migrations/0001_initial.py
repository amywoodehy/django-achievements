# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('key', models.CharField(max_length=75, unique=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('category', models.CharField(default='', max_length=75)),
                ('bonus', models.IntegerField(default=0)),
                ('callback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAchievement',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('achievement', models.ForeignKey(to='achievements.Achievement', related_name='userachievements')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
