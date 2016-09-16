# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_kakuser_project_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kakuser',
            old_name='project_id',
            new_name='project',
        ),
        migrations.AlterField(
            model_name='kakuser',
            name='is_admin',
            field=models.CharField(default=b'0', max_length=100, choices=[(b'1', b'Super User'), (b'0', b'Normal User'), (b'2', b'Staff User')]),
        ),
    ]
