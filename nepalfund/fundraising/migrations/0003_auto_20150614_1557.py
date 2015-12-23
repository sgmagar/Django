# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0002_auto_20150607_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gofundme',
            name='campaign',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='gofundme',
            name='created_by',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='gofundme',
            name='date_closed',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='gofundme',
            name='date_created',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='gofundme',
            name='donors_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='gofundme',
            name='goal',
            field=models.DecimalField(max_digits=11, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='gofundme',
            name='location',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='gofundme',
            name='total',
            field=models.DecimalField(max_digits=11, decimal_places=2, blank=True),
        ),
    ]
