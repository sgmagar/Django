# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0017_auto_20150622_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='extra_field_1',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tabledata',
            name='extra_field_1',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
