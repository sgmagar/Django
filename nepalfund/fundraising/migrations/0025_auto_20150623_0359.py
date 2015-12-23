# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0024_delete_corporate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabledata',
            name='name',
            field=models.CharField(help_text=b'Name of column. Leave this in blank to disable this column', max_length=200, null=True, blank=True),
        ),
    ]
