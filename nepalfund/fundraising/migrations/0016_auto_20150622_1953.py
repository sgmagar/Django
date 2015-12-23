# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0015_table_last_updated_activate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='aid_amount',
            new_name='aid_amount_activate',
        ),
    ]
