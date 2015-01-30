# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0007_auto_20150127_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='submitDate',
            field=models.DateTimeField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='viewDate',
            field=models.DateTimeField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
