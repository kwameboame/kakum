# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20160705_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuecomment',
            name='issue_resolved',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='issuecomment',
            name='location',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
