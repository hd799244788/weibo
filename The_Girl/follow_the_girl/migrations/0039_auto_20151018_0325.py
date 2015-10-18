# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0038_auto_20151018_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_follow_info',
            name='user_id',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
    ]
