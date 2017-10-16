# -*- coding: utf-8 -*-
from django.conf.urls import url

# 类视图
from django.views.generic import TemplateView

from . import views
# import testdb

urlpatterns = [

    url(r'^$',views.index,name="index"),
    url(r'^index/$',views.index,name="index"),
    url(r'^user_list/$',views.user_list,name="user_list_url"),
    url(r'^cbv/$', views.UListView.as_view()),
    # url(r'^about/', views.AboutView.as_view()),    
    url(r'^edit/(?P<user_id>[0-9]+)/$',views.edit,name="edit"),
    url(r'^del/(?P<user_id>[0-9]+)/$',views.delete,name="del"),
    url(r'^regist/$',views.regist,name="regist_url"),
    url(r'^api/$',views.api,name="api"),
    url(r'^login/$',views.login,name="login_url"),
    url(r'^logout/$',views.logout,name="logout_url"),
    # url(r'^upload/(?P<path>.*)', 'django.views.static.serve', {'document_root': '/home/lmm/Documents/gitworkspace/python/myproject/upload'}),     
    
    # url(r'^thankyou/$',views.thankyou,name="thank_you"),
    # url(r'^edit/(?P<tweet_id>[0-9]+)/$',views.post_tweet,name="edit"),
       
]
