# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20160722_0534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kakuser',
            old_name='project',
            new_name='project_id',
        ),
    ]
