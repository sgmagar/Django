# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0003_auto_20150614_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gofundme',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
