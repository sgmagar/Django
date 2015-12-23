# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0023_auto_20150623_0145'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Corporate',
        ),
    ]
