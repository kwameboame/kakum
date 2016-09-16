# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20160713_0929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ('title',), 'verbose_name_plural': 'Issues'},
        ),
    ]
