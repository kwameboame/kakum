# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20160721_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('image', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(related_name='gallery_pictures', to='projects.Project')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Gallery Picture',
            },
        ),
        migrations.CreateModel(
            name='GalleryVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('video', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('media_url', models.CharField(max_length=4000, null=True, blank=True)),
                ('project', models.ForeignKey(related_name='gallery_videos', to='projects.Project')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Gallery Video',
            },
        ),
        migrations.RemoveField(
            model_name='knowledgevideo',
            name='project',
        ),
        migrations.DeleteModel(
            name='KnowledgeVideo',
        ),
    ]
