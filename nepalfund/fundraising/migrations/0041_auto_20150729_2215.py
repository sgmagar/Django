# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0040_surveyextraquestion_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='first_name',
            field=models.CharField(max_length=200, null=True, verbose_name=b'First Name', blank=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='last_name',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Last Name', blank=True),
        ),
    ]
