# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0004_user_headimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qsbk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('pic_name', models.CharField(max_length=50, verbose_name='\u56fe\u7247\u540d\u79f0')),
                ('pic_url', models.CharField(max_length=300, verbose_name='\u56fe\u7247\u540d\u79f0')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
        ),
    ]
