# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import invites.models


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0013_auto_20150129_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='address',
            field=models.TextField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='token',
            field=models.CharField(default=invites.models.tokengenerator, unique=True, max_length=7, blank=True),
            preserve_default=True,
        ),
    ]
