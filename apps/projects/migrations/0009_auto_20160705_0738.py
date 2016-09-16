# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20160705_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuecomment',
            name='latitude',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='issuecomment',
            name='longitude',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
