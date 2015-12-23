# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0013_table_tabledata'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='description',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='table',
            name='name_activate',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(default=b'Name', max_length=30, null=True, blank=True),
        ),
    ]
