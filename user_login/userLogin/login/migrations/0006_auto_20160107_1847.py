# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20160107_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='holiday_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 7, 18, 47, 5, 770107, tzinfo=utc)),
        ),
    ]
