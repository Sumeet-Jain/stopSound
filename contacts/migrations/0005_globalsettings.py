# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20141104_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_option', models.CharField(max_length=200)),
                ('current_use_count', models.IntegerField(default=0)),
                ('sound_level', models.FloatField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
