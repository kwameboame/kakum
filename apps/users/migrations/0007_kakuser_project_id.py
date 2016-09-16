# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160628_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='kakuser',
            name='project_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
