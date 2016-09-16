# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Comment Category',
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=500, null=True, blank=True)),
                ('description', models.CharField(max_length=5000, null=True, blank=True)),
                ('author', models.ForeignKey(related_name='mysubmissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IssueComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField(max_length=3000)),
                ('image', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('video', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('audio', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('author', models.ForeignKey(related_name='my_comments', to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(related_name='issue_comments', to='projects.Issue')),
                ('rating_value', models.ForeignKey(to='projects.CommentCategory')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Issue Comments',
            },
        ),
        migrations.CreateModel(
            name='IssueImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('issue', models.ForeignKey(related_name='images', to='projects.Issue')),
            ],
        ),
        migrations.CreateModel(
            name='IssueVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('video', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('issue', models.ForeignKey(related_name='videos', to='projects.Issue')),
            ],
        ),
        migrations.CreateModel(
            name='KnowledgeCenterArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('image', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Knowledge Center Documents',
            },
        ),
        migrations.CreateModel(
            name='KnowledgeCenterAudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('audio', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Knowledge Center Documents',
            },
        ),
        migrations.CreateModel(
            name='KnowledgeCenterDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('document', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Knowledge Center Documents',
            },
        ),
        migrations.CreateModel(
            name='KnowledgeCenterVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('video', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Knowledge Center Video',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=100)),
                ('image', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='knowledgecentervideo',
            name='project',
            field=models.ForeignKey(related_name='knowledge_video', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='knowledgecenterdocument',
            name='project',
            field=models.ForeignKey(related_name='knowledge_document', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='knowledgecenteraudio',
            name='project',
            field=models.ForeignKey(related_name='knowledge_audio', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='knowledgecenterarticle',
            name='project',
            field=models.ForeignKey(related_name='knowledge_article', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(related_name='myissues', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='commentcategory',
            name='issue',
            field=models.ForeignKey(related_name='mycategory', to='projects.Issue'),
        ),
    ]
