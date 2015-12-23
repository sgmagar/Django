# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0054_alldata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alldata',
            name='aidType',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='alldata',
            name='amount',
            field=models.DecimalField(default=True, max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='alldata',
            name='dateType',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='alldata',
            name='donorName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='alldata',
            name='recipientCountry',
            field=models.CharField(max_length=70, blank=True),
        ),
        migrations.AlterField(
            model_name='alldata',
            name='sector',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='alldata',
            name='source',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='alldata',
            name='transactionDate',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='alldata',
            name='transactionType',
            field=models.CharField(max_length=40, blank=True),
        ),
    ]
