# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0004_delete_tb_follower_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_follower_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('place', models.CharField(max_length=128)),
                ('constellation', models.CharField(max_length=128)),
                ('brief_introduction', models.CharField(max_length=128)),
                ('mail', models.EmailField(max_length=75)),
                ('blog_address', models.URLField()),
                ('relationship', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
