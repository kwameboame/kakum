# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20160720_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='knowledgedocument',
            old_name='link',
            new_name='media_link',
        ),
        migrations.AlterField(
            model_name='issuecomment',
            name='media_url',
            field=models.CharField(max_length=4000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='issuevideo',
            name='media_url',
            field=models.CharField(max_length=4000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='knowledgeaudio',
            name='media_url',
            field=models.CharField(max_length=4000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='knowledgevideo',
            name='media_url',
            field=models.CharField(max_length=4000, null=True, blank=True),
        ),
    ]
