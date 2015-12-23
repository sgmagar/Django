# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0011_gofundme_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gofundme',
            name='goal',
            field=models.CharField(default=datetime.datetime(2015, 6, 21, 19, 23, 18, 771029, tzinfo=utc), max_length=200, blank=True),
            preserve_default=False,
        ),
    ]
