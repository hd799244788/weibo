# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0011_tb_counter_tb_favor_tb_follower_info_tb_weibo_test_test1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='test',
        ),
        migrations.DeleteModel(
            name='test1',
        ),
        migrations.AddField(
            model_name='tb_counter',
            name='use_id',
            field=models.OneToOneField(default=1, to='follow_the_girl.tb_follower_info'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tb_follower_info',
            name='password',
            field=models.CharField(default=7, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tb_follower_info',
            name='use_id',
            field=models.IntegerField(default=100000, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tb_follower_info',
            name='usename',
            field=models.CharField(default=2, max_length=128),
            preserve_default=False,
        ),
    ]
