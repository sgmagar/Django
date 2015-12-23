# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0034_auto_20150723_2212'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SurveyAnswer',
            new_name='SurveyExtraAnswer',
        ),
    ]
