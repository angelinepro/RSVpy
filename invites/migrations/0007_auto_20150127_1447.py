# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0006_remove_person_notcoming'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='coming',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
    ]
