# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_has_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
    ]
