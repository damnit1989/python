# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.forms import ModelForm
from django.template import RequestContext

# django内置加密, 以及验证
from django.contrib.auth.hashers import make_password, check_password
from poster.models import User
import json

# Create your views here.


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')

# 首页        
def index(request):
    # 读取cookie的值
    # username = request.COOKIES.get('username','')
    
    # 读取session的值
    username = request.session.get('username','')
    if username:
        return render(request,'index.html',{'username':username})    
        # return HttpResponse('首页登录成功!'+username)
    else:
        return HttpResponseRedirect('/online/login/')        


# 注册
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            new_password = make_password(password)            
            User.objects.create(username = username,password = new_password)
            str = '<a href="http://192.168.17.134:8000/online/login/">登录</a>'
            return HttpResponse('regist success!!' + str)
    else:
        uf = UserForm()
    return render(request,'regist.html',{'form':uf})


# 登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # new_password = make_password(password)
            
            # filter 返回queryset, get返回对象
            # userInfo = User.objects.filter(username__exact = username,password__exact = new_password)
            # userInfo = User.objects.filter(username__exact = username)
            try:
                userInfo = User.objects.get(username__exact = username)
                if userInfo:
                    if check_password(password,userInfo.password):
                        response = HttpResponseRedirect('/online/index/')
                        # 设置cookie
                        # response.set_cookie('username',username,3600)
                        
                        # 设置session
                        request.session['username'] = username                        
                        return response
                else:
                    return HttpResponseRedirect('/online/login/')
            except Exception, e:
                L = {}
                L['status'] = 0
                L['info'] = '发生异常'
                L['data'] = ''
                json_str = json.dumps(L)
                # return HttpResponse(e)# 打印异常信息
                return HttpResponse(json_str, content_type="application/json")
                # return HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
    return render(request,'login.html',{'form':uf})
    # return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(request))
    
    
# 登出
def logout(request):
    # pass
    response = HttpResponseRedirect('/online/index/')
    # 删除cookie
    response.delete_cookie('username')
    # 删除session
    del request.session['username']
    return response    