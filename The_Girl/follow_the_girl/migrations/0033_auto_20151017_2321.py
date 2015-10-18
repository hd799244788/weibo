# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0032_remove_tb_follow_info_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_counter',
            name='fans',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tb_counter',
            name='follow',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tb_counter',
            name='tc',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tb_follow_info',
            name='weibo_id',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
    ]
