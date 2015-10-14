# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0012_auto_20151013_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_counter',
            name='use_id',
            field=models.OneToOneField(default=10000, to='follow_the_girl.tb_follower_info'),
            preserve_default=True,
        ),
    ]
