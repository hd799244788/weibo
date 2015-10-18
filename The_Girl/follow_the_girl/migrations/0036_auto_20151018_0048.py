# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0035_tb_follow_info_profile_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_follow_info',
            name='fans_add',
            field=models.CharField(default=5, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tb_follow_info',
            name='follow_add',
            field=models.CharField(default=7, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tb_follow_info',
            name='tc_add',
            field=models.CharField(default=5, max_length=128),
            preserve_default=False,
        ),
    ]
