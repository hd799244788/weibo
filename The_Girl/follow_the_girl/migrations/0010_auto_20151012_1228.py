# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0009_test1'),
    ]

    operations = [
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
        migrations.DeleteModel(
            name='test',
        ),
        migrations.DeleteModel(
            name='test1',
        ),
    ]
