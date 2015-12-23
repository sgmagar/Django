# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0046_auto_20150731_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiplechoice',
            name='choice',
            field=models.CharField(help_text=b'Answer for multiple choice question', max_length=200, null=True, blank=True),
        ),
    ]
