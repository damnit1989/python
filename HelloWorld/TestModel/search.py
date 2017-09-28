# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
def search_form(request):

    return render(request,'search.html')
    # return HttpResponse('Hello World how are you!')

def search_get(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        # message = '你搜索的内容为:'+request.GET['q'].decode(UTF8)
        message = request.method

    else:
        # message = "你提交了空表单"
        message = "2222"
    # print('33333')        
    return HttpResponse(message)

def search_post(request):
    request.encoding = 'utf-8'
    if request.POST:
        return HttpResponse('is post')
    else:
        return HttpResponse('not post')        