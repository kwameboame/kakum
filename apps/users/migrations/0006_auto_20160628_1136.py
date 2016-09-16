# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160627_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakuser',
            name='avatar',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
    ]
