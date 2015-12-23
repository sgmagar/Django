# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0049_auto_20151218_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='date',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
