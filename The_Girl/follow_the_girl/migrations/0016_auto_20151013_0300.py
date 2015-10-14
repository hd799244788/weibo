# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0015_auto_20151013_0253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_counter',
            name='use',
        ),
        migrations.DeleteModel(
            name='tb_counter',
        ),
        migrations.DeleteModel(
            name='tb_favor',
        ),
        migrations.DeleteModel(
            name='tb_follower_info',
        ),
        migrations.DeleteModel(
            name='tb_weibo',
        ),
    ]
