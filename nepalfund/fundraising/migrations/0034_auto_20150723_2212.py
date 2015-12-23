# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0033_auto_20150721_0150'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SurveyQuestion',
            new_name='SurveyExtraQuestion',
        ),
        migrations.AddField(
            model_name='surveyanswer',
            name='survey',
            field=models.ForeignKey(default=1, to='fundraising.Survey', help_text=b'Survey'),
            preserve_default=False,
        ),
    ]
