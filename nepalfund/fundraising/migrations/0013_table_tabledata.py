# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0012_auto_20150621_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('table', models.CharField(unique=True, max_length=200)),
                ('name', models.BooleanField(default=True)),
                ('url', models.BooleanField(default=True)),
                ('aid_amount', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TableData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('aid_amount', models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('table', models.ForeignKey(to='fundraising.Table')),
            ],
        ),
    ]
