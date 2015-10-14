# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0016_auto_20151013_0300'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_counter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('follow', models.IntegerField()),
                ('funs', models.IntegerField()),
                ('posts', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tb_favor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favor_picture', models.URLField()),
                ('favor_music', models.URLField()),
                ('favor_place', models.URLField()),
                ('favor_movie', models.URLField()),
                ('favor_weibo', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tb_follower_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('use_id', models.IntegerField(default=100000, unique=True)),
                ('usename', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
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
        migrations.AddField(
            model_name='tb_counter',
            name='use',
            field=models.OneToOneField(default=10000, to='follow_the_girl.tb_follower_info'),
            preserve_default=True,
        ),
    ]
