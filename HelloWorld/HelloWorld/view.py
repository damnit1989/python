# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Test

#import pdf lib
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def hello(request):
    context = {}
    context['hello'] = 'Hello,World !'
    context['name'] = 'lmm'

    context['athlete_list'] = ['one','two','three']
    sql_data = Test.objects.filter(name='runoob')
    context['sql_data'] = sql_data
    return render(request,'hello.html',context)
    # return HttpResponse('Hello World how are you!')
    
def out_pdf(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment;filename = "test.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 100, "Hello world.")    
    p.showPage()
    p.save()
    return response
    