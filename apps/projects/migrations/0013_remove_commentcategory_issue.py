# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20160713_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentcategory',
            name='issue',
        ),
    ]
