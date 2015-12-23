# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0009_auto_20150623_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='corporate',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2015, 6, 19, 23, 25, 1, 332374, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
