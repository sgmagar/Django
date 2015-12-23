# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0014_auto_20150622_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='last_updated_activate',
            field=models.BooleanField(default=True),
        ),
    ]
