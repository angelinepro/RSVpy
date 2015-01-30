# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0010_auto_20150129_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='address',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
