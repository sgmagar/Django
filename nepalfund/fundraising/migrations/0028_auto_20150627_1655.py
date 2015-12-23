# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0027_auto_20150626_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundraiser',
            name='raised',
            field=models.DecimalField(null=True, max_digits=14, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='gofundme',
            name='total',
            field=models.DecimalField(null=True, max_digits=14, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='tabledata',
            name='aid_amount',
            field=models.DecimalField(null=True, max_digits=14, decimal_places=2, blank=True),
        ),
    ]
