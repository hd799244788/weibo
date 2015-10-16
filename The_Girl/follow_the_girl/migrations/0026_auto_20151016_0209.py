# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_the_girl', '0025_auto_20151016_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_counter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('use_id', models.CharField(unique=True, max_length=128)),
                ('follow', models.CharField(unique=True, max_length=128)),
                ('fans', models.CharField(unique=True, max_length=128)),
                ('tc', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tb_follow_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('use_id', models.CharField(max_length=128)),
                ('place', models.CharField(max_length=128)),
                ('constellation', models.CharField(max_length=128)),
                ('brief_introduction', models.CharField(max_length=128)),
                ('mail', models.CharField(max_length=128)),
                ('blog_address', models.CharField(max_length=128)),
                ('relationship', models.CharField(max_length=128)),
                ('level', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='page',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
