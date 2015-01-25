# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0002_party_head'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='Head',
            field=models.ForeignKey(to='invites.Person', null=True),
            preserve_default=True,
        ),
    ]
