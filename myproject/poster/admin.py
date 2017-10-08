# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *
# Register your models here.


class TweetAdmin(admin.ModelAdmin):
    #让对象显示字段
    list_display = ('text','author_email','created_at','state')
    
admin.site.register(Tweet, TweetAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','text','created_at')
admin.site.register(Comment)