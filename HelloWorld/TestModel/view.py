# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from .models import Test,article

#import pdf lib
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .forms import NameForm


def index(request):
    # 重定向到另一个url
    return redirect('/hello/list/')
    # return HttpResponse('首页!') 

    
def hello(request):
    context = {}
    context['hello'] = 'Hello,World !'
    context['name'] = 'lmm'

    context['athlete_list'] = ['one','two','three']
    # sql_data = Test.objects.filter(name='runoob')
    all_sql_data = Test.objects.all()    
    context['sql_data'] = all_sql_data

    
    #按照create_data降序排序，'-'表示降序，不加表示正序
    # context['article_list'] = article.objects.all().order_by('-create_date')
    
    #获取5条记录
    context['article_list'] = article.objects.all()[:5]
    
    # album_data = Test.objects.filter(title = '4455')
    # context['album_data'] = album_data
    return render(request,'hello.html',context)
    # return HttpResponse('Hello World how are you!')


def add_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        art = articel(title = title,text = text)
        art.save()
    return HttpResponseRedirect('/hello/list/')

def detail(request,id):
    context = {}
    detail = article.objects.filter(id = id)
    context['detail'] = detail
    return render(request,'detail.html',context)
    
    
def out_pdf(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment;filename = "test.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 100, "Hello world.")    
    p.showPage()
    p.save()
    return response


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # name = request.POST['your_name']
            T = Test(name = request.POST['your_name'])
            T.save()
            return redirect('/hello/list/')
            # return HttpResponseRedirect('/hello/list/')
    else:
        form = NameForm()
    return render(request,'form.html',{'form':form})