# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Test
def hello(request):
    context = {}
    context['hello'] = 'Hello,World !'
    context['name'] = 'lmm'

    context['athlete_list'] = ['one','two','three']
    sql_data = Test.objects.filter(name='runoob')
    context['sql_data'] = sql_data
    return render(request,'hello.html',context)
    # return HttpResponse('Hello World how are you!')