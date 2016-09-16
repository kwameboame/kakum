# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_auto_20160910_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedocument',
            name='title',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
