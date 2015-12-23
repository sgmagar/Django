# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0031_auto_20150713_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('email', models.CharField(max_length=200, null=True, blank=True)),
                ('phone', models.CharField(max_length=200, null=True, blank=True)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('crowdfunding', models.CharField(max_length=200, null=True, blank=True)),
                ('goal', models.CharField(max_length=200, null=True, blank=True)),
                ('campaign_time', models.CharField(max_length=200, null=True, blank=True)),
                ('goal_reached', models.BooleanField(default=False)),
                ('raised', models.CharField(max_length=200, null=True, blank=True)),
                ('used_ngo', models.BooleanField(default=False)),
                ('ngo', models.CharField(max_length=200, null=True, blank=True)),
                ('ngo_fee', models.CharField(max_length=200, null=True, blank=True)),
                ('ngo_cost', models.CharField(max_length=200, null=True, blank=True)),
                ('used_ingo', models.BooleanField(default=False)),
                ('ingo', models.CharField(max_length=200, null=True, blank=True)),
                ('ingo_fee', models.CharField(max_length=200, null=True, blank=True)),
                ('ingo_cost', models.CharField(max_length=200, null=True, blank=True)),
                ('visited', models.BooleanField(default=False)),
                ('visited_area', models.CharField(max_length=200, null=True, blank=True)),
                ('worked_with_team', models.BooleanField(default=False)),
                ('distributed_materials', models.BooleanField(default=False)),
                ('type_of_work', models.CharField(max_length=200, null=True, blank=True)),
                ('time_on_site', models.CharField(max_length=200, null=True, blank=True)),
                ('staying_location', models.CharField(max_length=200, null=True, blank=True)),
                ('visit_expense', models.CharField(max_length=200, null=True, blank=True)),
                ('how_support', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
    ]
