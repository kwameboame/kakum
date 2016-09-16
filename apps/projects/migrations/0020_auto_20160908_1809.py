# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20160908_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledgearticle',
            name='description',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
    ]
