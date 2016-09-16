# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20160910_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakuser',
            name='email',
            field=models.EmailField(default=b'SE4OYKRU2m@gmail.com', unique=True, max_length=255, verbose_name='email address'),
        ),
    ]
