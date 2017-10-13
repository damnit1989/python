# -*- coding: utf-8 -*-
# 自定义中间件


from django import http 
from django.utils.deprecation import MiddlewareMixin


class BlockedIpMiddleware(MiddlewareMixin):

    def process_request(self,request):
        if request.method == 'POST':
            if request.POST['username'] == 'admin':
                return http.HttpResponseForbidden(u'<h1>'+request.POST['username']+'  is con\'t login Forbidden</h1>')
        
        # 获取客户端IP
        if request.META['REMOTE_ADDR']:
            print '【Client request ip】：'+request.META['REMOTE_ADDR']
            # return http.HttpResponseForbidden('<h1>Forbidden</h1>')