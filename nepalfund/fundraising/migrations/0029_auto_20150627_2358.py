# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0028_auto_20150627_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='aid_amount_activate',
            new_name='aid_amount',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='url_activate',
            new_name='url',
        ),
    ]
