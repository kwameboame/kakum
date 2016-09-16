# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20160811_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakuser',
            name='email',
            field=models.EmailField(default=b'k98SFfIRY3@gmail.com', unique=True, max_length=255, verbose_name='email address'),
        ),
    ]
