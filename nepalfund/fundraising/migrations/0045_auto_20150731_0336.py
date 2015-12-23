# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0044_surveyextraquestion_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyextraquestion',
            name='types',
        ),
        migrations.AddField(
            model_name='surveyextraquestion',
            name='type_of_input',
            field=models.CharField(default=b'text', help_text=b'Type of input field', max_length=20, choices=[(b'text', b'Text'), (b'check', b'Check')]),
        ),
    ]
