# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0030_auto_20150712_2209'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='SurveyAnswer',
        ),
        migrations.RenameModel(
            old_name='Survey',
            new_name='SurveyQuestion',
        ),
    ]
