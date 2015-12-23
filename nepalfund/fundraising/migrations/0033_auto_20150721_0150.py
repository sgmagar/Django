# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0032_survey'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='survey',
            name='last_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='organization_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
