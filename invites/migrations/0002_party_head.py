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
            name='Head',
            field=models.ForeignKey(default=None, to='invites.Person'),
            preserve_default=True,
        ),
    ]
