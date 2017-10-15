# -*- coding: utf-8 -*-
# 自定义中间件


from django import http 
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

class BlockedIpMiddleware(MiddlewareMixin):

    def process_request(self,request):

        # 测试系统自带的认证系统
        # 匹配如果不是后台登录,则验证用户是否登录，
        if request.path != '/admin/' and request.path != '/admin/login/' and request.path != '/accounts/login/':
            if not request.user.is_authenticated():
                return HttpResponseRedirect('/accounts/login/')
        if request.method == 'POST':
            if request.POST['username'] == 'admin':
                pass
                # return http.HttpResponseForbidden(u'<h1>测试中间件 '+request.POST['username']+'  is con\'t login Forbidden</h1>')
        
        # 获取客户端IP
        if request.META['REMOTE_ADDR']:
            print '【Client request ip】：'+request.META['REMOTE_ADDR']
            # return http.HttpResponseForbidden('<h1>Forbidden</h1>')