# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0023_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='use_id',
            field=models.IntegerField(default=5, unique=True),
            preserve_default=False,
        ),
    ]
