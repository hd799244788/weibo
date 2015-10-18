# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0034_tb_follow_info_screen_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_follow_info',
            name='profile_image_url',
            field=models.CharField(default=6, max_length=128),
            preserve_default=False,
        ),
    ]
