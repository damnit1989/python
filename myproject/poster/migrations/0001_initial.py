# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 04:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300, verbose_name='\u5ba1\u6279')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140, verbose_name='\u5185\u5bb9')),
                ('author_email', models.CharField(max_length=200, verbose_name='\u4f5c\u8005email')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('published_at', models.DateTimeField(null=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('state', models.CharField(choices=[('pending', 'pending'), ('published', 'published'), ('rejected', 'rejected')], max_length=15, verbose_name='\u72b6\u6001')),
            ],
            options={
                'permissions': (('can_approver_or_reject_tweet', 'Can approver or reject tweets'),),
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poster.Tweet'),
        ),
    ]
