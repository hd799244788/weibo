# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0037_auto_20151018_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_follow_info',
            name='user_id',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
