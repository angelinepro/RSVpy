# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import invites.models


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0011_auto_20150129_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='token',
            field=models.CharField(default=invites.models.tokengenerator, max_length=7),
            preserve_default=True,
        ),
    ]
