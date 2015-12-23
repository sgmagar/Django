# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoFundMe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('campaign', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('goal', models.DecimalField(max_digits=11, decimal_places=2)),
                ('total', models.DecimalField(max_digits=11, decimal_places=2)),
                ('donors_number', models.IntegerField()),
                ('created_by', models.CharField(max_length=30)),
                ('date_created', models.DateField()),
                ('date_closed', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='fundraiser',
            name='fundraiser',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='fundraiser',
            name='raised',
            field=models.DecimalField(max_digits=11, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='fundraiser',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
