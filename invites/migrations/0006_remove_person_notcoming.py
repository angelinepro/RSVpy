# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0005_auto_20150127_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='notcoming',
        ),
    ]
