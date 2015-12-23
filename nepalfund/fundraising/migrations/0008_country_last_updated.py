# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0007_auto_20150619_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2015, 6, 19, 23, 9, 19, 54192, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
