# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0036_auto_20150723_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
