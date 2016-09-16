# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('image', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(related_name='knowledge_article', to='projects.Project')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Knowledge Article',
            },
        ),
        migrations.CreateModel(
            name='KnowledgeAudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('audio', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(related_name='knowledge_audio', to='projects.Project')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Knowledge Audio',
            },
        ),
        migrations.CreateModel(
            name='KnowledgeDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('document', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(related_name='knowledge_document', to='projects.Project')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Knowledge Docs',
            },
        ),
        migrations.CreateModel(
            name='KnowledgeVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('video', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(related_name='knowledge_video', to='projects.Project')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Knowledge Center Video',
            },
        ),
        migrations.RemoveField(
            model_name='knowledgecenterarticle',
            name='project',
        ),
        migrations.RemoveField(
            model_name='knowledgecenteraudio',
            name='project',
        ),
        migrations.RemoveField(
            model_name='knowledgecenterdocument',
            name='project',
        ),
        migrations.RemoveField(
            model_name='knowledgecentervideo',
            name='project',
        ),
        migrations.DeleteModel(
            name='KnowledgeCenterArticle',
        ),
        migrations.DeleteModel(
            name='KnowledgeCenterAudio',
        ),
        migrations.DeleteModel(
            name='KnowledgeCenterDocument',
        ),
        migrations.DeleteModel(
            name='KnowledgeCenterVideo',
        ),
    ]
