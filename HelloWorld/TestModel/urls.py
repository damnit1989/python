# -*- coding: utf-8 -*-
from django.conf.urls import url


from . import view,search,testdb
# import testdb

urlpatterns = [

    url(r'^$',view.hello,name="hello"),
    # url(r'^hello/',view.hello),
    # url(r'^search_form/',search.search_form),
    # url(r'^search_get',search.search_get),
    # url(r'^search_post',search.search_post),
    # url(r'^testdb$', testdb.testdb),    
    # url(r'^test_articel_db$', testdb.testArticleDb),    
    # url(r'^pdf$', view.out_pdf),    
    # url(r'^view/hello/$', view.hello),
]
