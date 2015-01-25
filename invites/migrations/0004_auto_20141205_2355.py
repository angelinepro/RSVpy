# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0003_auto_20141205_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='Party',
        ),
        migrations.AddField(
            model_name='party',
            name='Members',
            field=models.ManyToManyField(to='invites.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='Head',
            field=models.ForeignKey(related_name='+', to='invites.Person'),
            preserve_default=True,
        ),
    ]
