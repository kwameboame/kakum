# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20160719_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledgearticle',
            name='show_on_homepage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='knowledgeaudio',
            name='show_on_homepage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='knowledgedocument',
            name='show_on_homepage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='knowledgevideo',
            name='show_on_homepage',
            field=models.BooleanField(default=False),
        ),
    ]
