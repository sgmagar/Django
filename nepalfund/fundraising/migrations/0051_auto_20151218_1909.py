# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0050_table_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='aid_amount',
            field=models.DecimalField(default=True, help_text=b'Aid Amount Column Field. Check to Enable this column. Uncheck to disable', max_digits=20, decimal_places=2),
        ),
    ]
