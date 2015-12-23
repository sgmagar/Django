# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0045_auto_20150731_0336'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='surveyextraquestion',
            name='type_of_input',
            field=models.CharField(default=b'text', help_text=b'Type of input field', max_length=20, choices=[(b'text', b'Text'), (b'check', b'Yes or No question'), (b'multiple_choice', b'Multiple Choice')]),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='question',
            field=models.ForeignKey(help_text=b'Choice for which question', to='fundraising.SurveyExtraQuestion'),
        ),
    ]
