# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20160624_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='has_expired',
            field=models.BooleanField(default=False),
        ),
    ]
