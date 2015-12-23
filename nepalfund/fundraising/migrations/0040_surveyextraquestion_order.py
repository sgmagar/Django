# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0039_auto_20150725_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyextraquestion',
            name='order',
            field=models.IntegerField(default=1, help_text=b'Set a number to question to sort them in order. The lower the number the higher it will be'),
            preserve_default=False,
        ),
    ]
