# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20160712_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuecomment',
            old_name='rating_value',
            new_name='rating',
        ),
        migrations.AlterField(
            model_name='issuecomment',
            name='comment_type',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Complaint', b'Complaint'), (b'Suggestion', b'Suggestion'), (b'Endorsement', b'Endorsement'), (b'Irrelevant', b'Irrelevant')]),
        ),
        migrations.AlterField(
            model_name='issuecomment',
            name='input_channel',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Web', b'Web'), (b'SMS', b'SMS'), (b'Email', b'Email'), (b'WhatsApp', b'WhatsApp'), (b'Facebook', b'Facebook'), (b'Twitter', b'Twitter'), (b'Offline', b'Offline')]),
        ),
    ]
