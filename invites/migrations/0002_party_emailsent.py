# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='emailSent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
