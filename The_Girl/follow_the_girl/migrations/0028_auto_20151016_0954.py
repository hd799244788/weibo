# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0027_tb_use_map_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_findout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('use_id', models.CharField(max_length=128)),
                ('picture', models.CharField(max_length=128)),
                ('screen_name', models.CharField(max_length=128)),
                ('loction', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
                ('followers_count', models.CharField(max_length=128)),
                ('friends_count', models.CharField(max_length=128)),
                ('statuses_count', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
