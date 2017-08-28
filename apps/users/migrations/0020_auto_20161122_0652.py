# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20160910_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakuser',
            name='email',
            field=models.EmailField(default=b'eBdYtP2Mx6@gmail.com', unique=True, max_length=255, verbose_name='email address'),
        ),
    ]
