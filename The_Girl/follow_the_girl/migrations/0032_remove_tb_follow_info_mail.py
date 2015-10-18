# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0031_auto_20151017_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_follow_info',
            name='mail',
        ),
    ]
