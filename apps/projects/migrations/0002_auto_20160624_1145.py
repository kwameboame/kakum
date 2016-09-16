# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=10000, null=True, blank=True),
        ),
    ]
