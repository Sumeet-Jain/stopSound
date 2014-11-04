# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20141102_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
