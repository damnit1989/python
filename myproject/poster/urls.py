# -*- coding: utf-8 -*-
from django.conf.urls import url


from . import views
# import testdb

urlpatterns = [

    url(r'^$',views.post_tweet,name="post_tweet"),
    url(r'^thankyou/$',views.thankyou,name="thank_you"),
    url(r'^edit/(?P<tweet_id>[0-9]+)/$',views.post_tweet,name="edit"),
]
