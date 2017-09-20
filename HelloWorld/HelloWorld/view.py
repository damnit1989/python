# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    context = {}
    context['hello'] = 'Hello,World !'
    context['name'] = 'lmm'

    context['athlete_list'] = ['one','two','three']
    return render(request,'hello.html',context)
    # return HttpResponse('Hello World how are you!')