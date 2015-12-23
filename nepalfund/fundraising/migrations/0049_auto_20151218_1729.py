# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0048_auto_20150923_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='table',
            name='subcategory',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
