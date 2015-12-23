# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0021_delete_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='extra_field_4',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tabledata',
            name='extra_field_4',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
