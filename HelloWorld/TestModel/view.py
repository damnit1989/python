# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from .models import Test,article

#import pdf lib
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def index(request):
    return HttpResponse('首页!') 

    
def hello(request):
    context = {}
    context['hello'] = 'Hello,World !'
    context['name'] = 'lmm'

    context['athlete_list'] = ['one','two','three']
    # sql_data = Test.objects.filter(name='runoob')
    all_sql_data = Test.objects.all()    
    context['sql_data'] = all_sql_data
    # article1 = article()
    context['article_list'] = article.objects.all()
    # album_data = Test.objects.filter(title = '4455')
    # context['album_data'] = album_data
    return render(request,'hello.html',context)
    # return HttpResponse('Hello World how are you!')


def detail(request,id):
    context = {}
    detail = article.objects.filter(id = id)
    context['detail'] = detail
    return render(request,'detail.html',content)
    
    
def out_pdf(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment;filename = "test.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 100, "Hello world.")    
    p.showPage()
    p.save()
    return response
    