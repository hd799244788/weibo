# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0005_tb_follower_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tb_follower_info',
        ),
    ]
