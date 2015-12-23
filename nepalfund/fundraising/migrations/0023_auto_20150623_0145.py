# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0022_auto_20150623_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='extra_field_5',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tabledata',
            name='extra_field_5',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
