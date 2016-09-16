# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.rest_api.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160627_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakuser',
            name='avatar',
            field=apps.rest_api.thumbs.ImageWithThumbsField(default=None, null=True, upload_to=b'NEW_CACHES/AVATARS/2016/06/27/14:48:22/', blank=True),
        ),
    ]
