# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0051_auto_20151218_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='gofundme',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gofundme',
            name='name',
            field=models.CharField(default=b'Name', max_length=100, null=True, help_text=b'Name of column. Leave this in blank to disable this column', blank=True),
        ),
        migrations.AddField(
            model_name='gofundme',
            name='subcategory',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
