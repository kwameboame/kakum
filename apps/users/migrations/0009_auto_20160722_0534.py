# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20160722_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakuser',
            name='project',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
