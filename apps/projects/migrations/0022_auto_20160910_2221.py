# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20160908_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryAlbum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Gallery Albubm',
            },
        ),
        migrations.CreateModel(
            name='RelevantLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000, null=True, blank=True)),
                ('link', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='gallerypicture',
            name='project',
        ),
        migrations.AddField(
            model_name='gallerypicture',
            name='album',
            field=models.ForeignKey(related_name='my_gallery_pictures', blank=True, to='projects.GalleryAlbum', null=True),
        ),
    ]
