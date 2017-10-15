# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myproject import settings
from django.db import models

# Create your models here.

class Tweet(models.Model):
    text = models.CharField(verbose_name = '内容', max_length = 140)
    author_email = models.CharField(verbose_name = '作者email', max_length = 200)
    created_at = models.DateTimeField(verbose_name = '创建时间', auto_now_add = True)
    published_at = models.DateTimeField(verbose_name = '发布时间', null = True)
    STATE_CHOICES = (
        ('pending', 'pending'),
        ('published', 'published'),
        ('rejected', 'rejected'),
    )
    state = models.CharField(verbose_name = '状态', max_length = 15, choices = STATE_CHOICES)
    
    def __unicode__(self):
        return self.text
    
    class Meta:
        permissions = (
            ("can_approver_or_reject_tweet","Can approver or reject tweets"),
        )
        
        
class Comment(models.Model):
    tweet = models.ForeignKey(Tweet)
    text = models.CharField(verbose_name = '审批', max_length = 300)
    created_at = models.DateTimeField(verbose_name = '创建时间', auto_now_add = True)
    
    def __unicode__(self):
        return self.text

class User(models.Model):
    username = models.CharField(verbose_name = '用户名', max_length = 20)
    password = models.CharField(verbose_name = '密码', max_length = 200)
    headImg = models.FileField(verbose_name = '用户头像',upload_to = settings.UPLOAD_FILE,null = True)
    def __unicode__(self):
        return self.username
        
    def get_user(self,user_id):
        user_info = self.objects.get(id = user_id)
        return user_info
    