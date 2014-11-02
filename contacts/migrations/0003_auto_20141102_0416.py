# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20141014_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='settings',
            name='name',
            field=models.CharField(default='boo', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='settings',
            name='sound_level',
            field=models.FloatField(),
        ),
    ]
