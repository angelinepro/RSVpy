# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0008_auto_20150127_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='inviteType',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
