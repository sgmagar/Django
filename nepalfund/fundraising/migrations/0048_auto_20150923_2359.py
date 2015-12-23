# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0047_auto_20150731_0525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='campaign_time',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='crowdfunding',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='description',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='distributed_materials',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='goal',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='goal_reached',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='how_support',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='ingo',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='ingo_cost',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='ingo_fee',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='ngo',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='ngo_cost',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='ngo_fee',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='raised',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='staying_location',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='time_on_site',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='type_of_work',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='used_ingo',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='used_ngo',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='visit_expense',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='visited',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='visited_area',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='worked_with_team',
        ),
    ]
