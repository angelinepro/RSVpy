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
                ('email', models.CharField(max_length=200)),
                ('emailInvite', models.BooleanField(default=True)),
                ('viewDate', models.DateTimeField(default=None, null=True, blank=True)),
                ('submitDate', models.DateTimeField(default=None, null=True, blank=True)),
                ('address', models.TextField(default=None)),
                ('token', models.CharField(db_index=True, unique=True, max_length=7, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Parties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('coming', models.NullBooleanField(default=None)),
            ],
            options={
                'verbose_name_plural': 'People',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SeenBrowser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('browser', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=64)),
                ('times', models.PositiveIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='party',
            name='head',
            field=models.ForeignKey(related_name='+', to='invites.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='members',
            field=models.ManyToManyField(to='invites.Person'),
            preserve_default=True,
        ),
    ]
