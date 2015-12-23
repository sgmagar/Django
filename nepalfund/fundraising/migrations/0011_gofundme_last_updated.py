# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0010_corporate_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='gofundme',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2015, 6, 19, 23, 58, 45, 73945, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
