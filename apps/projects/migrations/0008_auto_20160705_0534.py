# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20160705_0459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuecomment',
            old_name='archive',
            new_name='archive_comment',
        ),
        migrations.AddField(
            model_name='issuecomment',
            name='comment_type',
            field=models.CharField(default=1, max_length=100, choices=[(b'Complaint', b'Complaint'), (b'Suggestion', b'Suggestion'), (b'Endorsement', b'Endorsement'), (b'Irrelevant', b'Irrelevant')]),
            preserve_default=False,
        ),
    ]
