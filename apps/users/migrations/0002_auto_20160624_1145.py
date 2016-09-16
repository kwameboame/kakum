# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.rest_api.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakuser',
            name='avatar',
            field=apps.rest_api.thumbs.ImageWithThumbsField(default=None, null=True, upload_to=b'NEW_CACHES/AVATARS/2016/06/24/11:45:30/', blank=True),
        ),
    ]
