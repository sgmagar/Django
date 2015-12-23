# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0016_auto_20150622_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='url',
            new_name='url_activate',
        ),
    ]
