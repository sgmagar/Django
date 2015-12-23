# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0052_auto_20151219_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='gofundme',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
