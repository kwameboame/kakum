# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20160811_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('document', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('cover_image', s3direct.fields.S3DirectField(null=True, blank=True)),
                ('media_url', models.CharField(max_length=4000, null=True, blank=True)),
                ('issue', models.ForeignKey(related_name='documents', to='projects.Issue')),
            ],
        ),
        migrations.RemoveField(
            model_name='knowledgearticle',
            name='date_created',
        ),
        migrations.AddField(
            model_name='knowledgearticle',
            name='date_published',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='knowledgedocument',
            name='cover_image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
    ]
