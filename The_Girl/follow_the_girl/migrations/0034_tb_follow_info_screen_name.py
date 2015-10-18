# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0033_auto_20151017_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_follow_info',
            name='screen_name',
            field=models.CharField(default=6, max_length=128),
            preserve_default=False,
        ),
    ]
