# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0037_auto_20150723_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
