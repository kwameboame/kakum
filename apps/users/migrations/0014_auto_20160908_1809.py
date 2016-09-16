# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20160908_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakuser',
            name='email',
            field=models.EmailField(default=b'FtHT0ciYfu@gmail.com', unique=True, max_length=255, verbose_name='email address'),
        ),
    ]
