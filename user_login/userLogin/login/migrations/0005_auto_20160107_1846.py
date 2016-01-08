# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20160107_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='holiday_date',
            field=models.DateField(default=datetime.date(2016, 1, 7)),
        ),
    ]
