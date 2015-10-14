# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0002_delete_tb_weibo'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_weibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weibo_info', models.URLField()),
                ('repeat_list', models.URLField()),
            ],
            options={
                'verbose_name': 'MODELNAME',
                'verbose_name_plural': 'MODELNAMEs',
            },
            bases=(models.Model,),
        ),
    ]
