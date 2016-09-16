# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_remove_commentcategory_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuecomment',
            name='link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='issuecomment',
            name='media_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='issuevideo',
            name='media_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='knowledgearticle',
            name='media_link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='knowledgeaudio',
            name='media_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='knowledgedocument',
            name='link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='knowledgevideo',
            name='media_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
