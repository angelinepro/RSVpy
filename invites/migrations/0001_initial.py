# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('Email', models.CharField(max_length=200)),
                ('ViewDate', models.DateTimeField(auto_now=True)),
                ('SubmitDate', models.DateTimeField(auto_now=True)),
                ('Address', models.CharField(max_length=500)),
                ('Token', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=50)),
                ('Coming', models.BooleanField(default=False)),
                ('Party', models.ForeignKey(to='invites.Party')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
