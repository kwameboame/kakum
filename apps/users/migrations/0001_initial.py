# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import apps.rest_api.thumbs


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KAKUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email address')),
                ('username', models.CharField(default=b'02000000', max_length=100, verbose_name='username')),
                ('first_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100, null=True, blank=True)),
                ('last_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.CharField(default=b'0', max_length=100, choices=[(b'1', b'Super User'), (b'0', b'Normal User')])),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('avatar', apps.rest_api.thumbs.ImageWithThumbsField(default=None, null=True, upload_to=b'NEW_CACHES/AVATARS/2016/06/24/09:36:51/', blank=True)),
                ('sm_avatar', models.URLField(default=None, null=True, verbose_name='Social Media Avatar', blank=True)),
            ],
            options={
                'ordering': ('id', 'first_name'),
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
