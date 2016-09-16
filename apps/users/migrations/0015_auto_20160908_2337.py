# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20160908_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakuser',
            name='email',
            field=models.EmailField(default=b'nwPYpNAErS@gmail.com', unique=True, max_length=255, verbose_name='email address'),
        ),
    ]
