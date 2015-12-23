# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0005_auto_20150614_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gofundme',
            name='campaign',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='gofundme',
            name='created_by',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='gofundme',
            name='date_closed',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='gofundme',
            name='date_created',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='gofundme',
            name='location',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
