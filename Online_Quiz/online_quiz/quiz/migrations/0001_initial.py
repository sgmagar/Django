# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer_Choice',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('position', models.IntegerField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='answer_choice',
            name='question_id',
            field=models.ForeignKey(to='quiz.Question'),
        ),
    ]
