# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20160629_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuecomment',
            name='archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='issuecomment',
            name='input_channel',
            field=models.CharField(default=1, max_length=100, choices=[(b'Web', b'Web'), (b'SMS', b'SMS'), (b'Email', b'Email'), (b'WhatsApp', b'WhatsApp'), (b'Facebook', b'Facebook'), (b'Twitter', b'Twitter'), (b'Offline', b'Offline')]),
            preserve_default=False,
        ),
    ]
