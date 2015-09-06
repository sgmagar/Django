# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer_choice',
            name='position',
        ),
        migrations.RemoveField(
            model_name='question',
            name='position',
        ),
        migrations.AddField(
            model_name='answer_choice',
            name='correct_choice',
            field=models.BooleanField(default=False),
        ),
    ]
