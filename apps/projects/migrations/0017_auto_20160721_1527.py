# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20160721_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='knowledgearticle',
            old_name='media_link',
            new_name='media_url',
        ),
        migrations.RenameField(
            model_name='knowledgedocument',
            old_name='media_link',
            new_name='media_url',
        ),
    ]
