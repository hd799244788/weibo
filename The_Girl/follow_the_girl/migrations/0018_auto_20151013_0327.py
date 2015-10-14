# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0017_auto_20151013_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_counter',
            name='use',
        ),
        migrations.AddField(
            model_name='tb_counter',
            name='use_id',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tb_follower_info',
            name='use_id',
            field=models.OneToOneField(default=True, to='follow_the_girl.tb_counter'),
            preserve_default=True,
        ),
    ]
