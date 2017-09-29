# -*- coding: utf-8 -*-

from django.contrib import admin
from TestModel.models import Test
from TestModel.models import Album
from TestModel.models import article


class articleAdmin(admin.ModelAdmin):
    #让对象显示字段
    list_display = ('title','create_date','publish_date')
   
   
# Register your models here.
admin.site.register(Test)
admin.site.register(Album)
# admin.site.register(article)
admin.site.register(article,articleAdmin)