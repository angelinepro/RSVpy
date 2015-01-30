# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0009_party_invitetype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='inviteType',
            new_name='emailInvite',
        ),
    ]
