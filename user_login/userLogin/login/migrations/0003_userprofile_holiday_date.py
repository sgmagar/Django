# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_userprofile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='holiday_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 7, 18, 26, 50, 814184)),
        ),
    ]
