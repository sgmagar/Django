# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0019_auto_20150622_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='name_activate',
        ),
        migrations.AlterField(
            model_name='table',
            name='extra_field_1',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='extra_field_2',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='extra_field_3',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(default=b'Name', max_length=40, null=True, blank=True),
        ),
    ]
