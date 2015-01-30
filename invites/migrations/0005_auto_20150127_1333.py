# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0004_auto_20141205_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='party',
            options={'verbose_name_plural': 'Parties'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.RenameField(
            model_name='party',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='party',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='party',
            old_name='Head',
            new_name='head',
        ),
        migrations.RenameField(
            model_name='party',
            old_name='Members',
            new_name='members',
        ),
        migrations.RenameField(
            model_name='party',
            old_name='Token',
            new_name='token',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='Coming',
            new_name='coming',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='Name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='party',
            name='SubmitDate',
        ),
        migrations.RemoveField(
            model_name='party',
            name='ViewDate',
        ),
        migrations.AddField(
            model_name='party',
            name='submitDate',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='viewDate',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='notcoming',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
