# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0035_auto_20150723_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='email',
            field=models.EmailField(default=1, unique=True, max_length=254, blank=True),
            preserve_default=False,
        ),
    ]
