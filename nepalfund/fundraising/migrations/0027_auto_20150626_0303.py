# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0026_auto_20150623_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='extra_field_6',
            field=models.CharField(help_text=b'Name of extra column. Leave this in blank to disable this column', max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='table',
            name='extra_field_7',
            field=models.CharField(help_text=b'Name of extra column. Leave this in blank to disable this column', max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tabledata',
            name='extra_field_6',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tabledata',
            name='extra_field_7',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
