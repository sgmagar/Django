# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0043_auto_20150729_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyextraquestion',
            name='types',
            field=models.CharField(default=b'text', max_length=20, choices=[(b'text', b'Text'), (b'check', b'Check')]),
        ),
    ]
