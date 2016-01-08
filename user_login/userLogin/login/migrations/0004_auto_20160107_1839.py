# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_userprofile_holiday_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='holiday_date',
            field=models.DateField(default=datetime.date),
        ),
    ]
