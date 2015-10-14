# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0021_auto_20151013_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_follower_info',
            name='use_id',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
    ]
