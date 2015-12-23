# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0038_auto_20150723_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyextraquestion',
            name='question',
            field=models.CharField(help_text=b'Label of extra field for the survey form', max_length=200, null=True, blank=True),
        ),
    ]
