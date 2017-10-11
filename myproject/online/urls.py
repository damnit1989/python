# -*- coding: utf-8 -*-
from django.conf.urls import url


from . import views
# import testdb

urlpatterns = [

    url(r'^$',views.index,name="index"),
    url(r'^index/$',views.index,name="index"),
    url(r'^user_list/$',views.user_list,name="user_list"),
    url(r'^edit/(?P<user_id>[0-9]+)/$',views.edit,name="edit"),
    url(r'^del/(?P<user_id>[0-9]+)/$',views.delete,name="del"),
    url(r'^regist/$',views.regist,name="regist"),
    url(r'^login/$',views.login,name="login"),
    url(r'^logout/$',views.logout,name="logout"),
    # url(r'^upload/(?P<path>.*)', 'django.views.static.serve', {'document_root': '/home/lmm/Documents/gitworkspace/python/myproject/upload'}),     
    
    # url(r'^thankyou/$',views.thankyou,name="thank_you"),
    # url(r'^edit/(?P<tweet_id>[0-9]+)/$',views.post_tweet,name="edit"),
       
]
