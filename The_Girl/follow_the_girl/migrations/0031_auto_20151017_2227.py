# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0030_auto_20151017_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tb_counter',
            old_name='use_id',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='tb_findout',
            old_name='picture',
            new_name='profile_image_url',
        ),
        migrations.RenameField(
            model_name='tb_findout',
            old_name='use_id',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='tb_follow_info',
            old_name='brief_introduction',
            new_name='fans',
        ),
        migrations.RenameField(
            model_name='tb_follow_info',
            old_name='constellation',
            new_name='follow',
        ),
        migrations.RenameField(
            model_name='tb_follow_info',
            old_name='level',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='tb_follow_info',
            old_name='relationship',
            new_name='tc',
        ),
        migrations.RenameField(
            model_name='tb_follow_info',
            old_name='use_id',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='tb_use_map_id',
            old_name='use_id',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='tb_use_map_id',
            old_name='use_name',
            new_name='user_name',
        ),
        migrations.AddField(
            model_name='tb_follow_info',
            name='weibo_id',
            field=models.CharField(default=7, max_length=128),
            preserve_default=False,
        ),
    ]
