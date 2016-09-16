# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20160909_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakuser',
            name='email',
            field=models.EmailField(default=b'C9bUm2kEtc@gmail.com', unique=True, max_length=255, verbose_name='email address'),
        ),
    ]
