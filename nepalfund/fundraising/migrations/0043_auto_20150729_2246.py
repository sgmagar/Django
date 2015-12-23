# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0042_auto_20150729_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyextraquestion',
            name='order',
            field=models.IntegerField(help_text=b'Set a number to this question to sort them in sequence. The lower the number the higher it will be in the list/survey', verbose_name=b'Order in the list'),
        ),
    ]
