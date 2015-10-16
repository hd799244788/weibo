# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0028_auto_20151016_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_struct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('w_id', models.CharField(max_length=128)),
                ('screen_name', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('profile_image_url', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=128)),
                ('followers_count', models.CharField(max_length=128)),
                ('friends_count', models.CharField(max_length=128)),
                ('statuses_count', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
