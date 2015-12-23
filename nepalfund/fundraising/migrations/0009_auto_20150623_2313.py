# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0008_country_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='last_updated',
            field=models.DateField(auto_now=True),
        ),
    ]
