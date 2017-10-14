# -*- coding: utf-8 -*-
# django上下文渲染器，给模板分配额外变量


from django.conf import settings as original_settings


def settings(request):
    return {'setting':original_settings}
    
    
def ip_address(request):
    return {
        'ip_address':request.META['REMOTE_ADDR'],
        'request_method':request.method,
    }
