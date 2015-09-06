# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20150905_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
