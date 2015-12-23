# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corporate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization', models.CharField(max_length=100)),
                ('aid_amount', models.DecimalField(max_digits=11, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=30)),
                ('aid_amount', models.DecimalField(max_digits=11, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Fundraiser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fundraiser', models.CharField(max_length=30)),
                ('url', models.URLField()),
                ('raised', models.DecimalField(max_digits=11, decimal_places=2)),
            ],
        ),
    ]
