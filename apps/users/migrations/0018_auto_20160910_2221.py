# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20160909_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakuser',
            name='email',
            field=models.EmailField(default=b'5YuY49aPwR@gmail.com', unique=True, max_length=255, verbose_name='email address'),
        ),
    ]
