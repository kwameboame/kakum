# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160624_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='knowledgecenterarticle',
            options={'ordering': ('-id',), 'verbose_name_plural': 'Knowledge Center Article'},
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(max_length=5000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='knowledgecenterarticle',
            name='description',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='knowledgecenteraudio',
            name='description',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='knowledgecenterdocument',
            name='description',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='knowledgecentervideo',
            name='description',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
    ]
