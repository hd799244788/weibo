# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0029_tb_struct'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_findout',
            name='weibo_id',
            field=models.CharField(default=6, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tb_use_map_id',
            name='use_name',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
    ]
