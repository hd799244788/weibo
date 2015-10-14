# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0019_auto_20151013_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tb_counter',
            old_name='posts',
            new_name='tc',
        ),
    ]
