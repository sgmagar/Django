# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0025_auto_20150623_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='aid_amount_activate',
            field=models.BooleanField(default=True, help_text=b'Aid Amount Column Field. Check to Enable this column. Uncheck to disable'),
        ),
        migrations.AlterField(
            model_name='table',
            name='description',
            field=models.TextField(help_text=b'Description of Table', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='extra_field_1',
            field=models.CharField(help_text=b'Name of extra column. Leave this in blank to disable this column', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='extra_field_2',
            field=models.CharField(help_text=b'Name of extra column. Leave this in blank to disable this column', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='extra_field_3',
            field=models.CharField(help_text=b'Name of extra column. Leave this in blank to disable this column', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='extra_field_4',
            field=models.CharField(help_text=b'Name of extra column. Leave this in blank to disable this column', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='extra_field_5',
            field=models.CharField(help_text=b'Name of extra column. Leave this in blank to disable this column', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='last_updated_activate',
            field=models.BooleanField(default=True, help_text=b'Last Updated Column Field. Check to Enable this column. Uncheck to disable'),
        ),
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(default=b'Name', max_length=40, null=True, help_text=b'Name of column. Leave this in blank to disable this column', blank=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='table',
            field=models.CharField(help_text=b'Name of Table', unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='table',
            name='url_activate',
            field=models.BooleanField(default=True, help_text=b'URL Column Field. Check to Enable this column. Uncheck to disable'),
        ),
        migrations.AlterField(
            model_name='tabledata',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tabledata',
            name='table',
            field=models.ForeignKey(help_text=b'Table name', to='fundraising.Table'),
        ),
    ]
