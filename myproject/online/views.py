# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound,Http404
from django import forms
from django.forms import ModelForm
from django.template import RequestContext

# django内置加密, 以及验证
from django.contrib.auth.hashers import make_password, check_password
from poster.models import User, Qsbk
import json

# 分页
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# 类视图
from django.views.generic import ListView,DetailView,TemplateView


# 导入爬虫的库开始
import urllib, urllib2
from bs4 import BeautifulSoup
import os
import threading

# Create your views here.

#用于注册的form表单
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','headImg')

# 用户登录的form表单，不包含头像
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
        
# 修改用户信息的表单
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',) 

class AboutView(TemplateView):
    template_name = "about.html"
    pass
    
# 首页        
def index(request):
    # 读取cookie的值
    # username = request.COOKIES.get('username','')
    
    # 读取session的值
    try:
        username = request.session.get('username','')
        userInfo = User.objects.get(username__exact = username)
        if username and userInfo:
            return render(request,'index.html',{'username':username,'info':userInfo})    
            # return HttpResponse('首页登录成功!'+username)
        else:
            return HttpResponseRedirect('/online/login/')
    except Exception, e:
        # return HttpResponse(e)
        return HttpResponseRedirect('/online/login/')

        
# 基于函数视图(fbv)
def user_list(request):
    # 查询所有的用户

    # 分页显示
    # user_list = User.objects.all()    
    contact_list = User.objects.all()
    paginator = Paginator(contact_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)  
    # 返回信息        
    return render_to_response('user_list.html', {"contacts": contacts})
    # return render(request,'user_list.html',{'user_list':user_list})

 
# 基于类视图(cbv) 
class UListView(ListView):
    template_name = 'online/user_list_class.html'
    
    # model = User 等同于queryset = User.objects.all()
    queryset = User.objects.order_by('-id')
    
    context_object_name = "user_list" 
    
    # 添加额外的上下文数据分配到模板
    def get_context_data(self,**kwargs):
        context = super(UListView, self).get_context_data(**kwargs)
        context['name_list'] = ['张三','李四','王麻子']
        
        # 在js中调用
        context['name_list_json'] = json.dumps(['张三','李四','王麻子'])
        return context

 
# 修改
def edit(request,user_id = None):
    try:
        userInfo = User.objects.get(id = user_id)
    except Exception, e:
        # 抛出404
        raise Http404("not find this userinfo")
        # return HttpResponseNotFound('not find this userinfo')
    if request.method == "POST":
        form = UserEditForm(request.POST,instance = userInfo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/online/user_list/')            
    else:
        uf = UserEditForm(instance = userInfo)
        return render(request,'edit.html',{'form':uf})
        
# 删除        
def delete(request,user_id = None):
    if user_id:
        User.objects.filter(id = user_id).delete()
    return HttpResponseRedirect('/online/user_list/')

    
# 注册
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            headImg = uf.cleaned_data['headImg']
            new_password = make_password(password)            
            User.objects.create(username = username,password = new_password,headImg = headImg)
            str = '<a href="http://192.168.17.134:8000/online/login/">登录</a>'
            return HttpResponse('regist success!!' + str)
    else:
        uf = UserForm()
    return render(request,'regist.html',{'form':uf})


# 登录
def login(request):
    if request.method == 'POST':
        uf = UserLoginForm(request.POST)
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
        uf = UserLoginForm()
    return render(request,'log_in.html',{'form':uf})
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


# liudao/curl_python_api.php调该接口
def api(request):
    return_php_data = {'name':'lmm','age':'34','height':'124','info':'请求成功'}
    data = json.dumps(return_php_data).encode('utf-8')    
    return HttpResponse(data, content_type="application/json")    



# ------------------------------------爬虫代码开始-------------------------------------    
# 写入文件
def write_to_file(content,filename):
    with open(filename,'a') as f:
        f.write(content.encode('utf-8'))

        
# 获取图片保存到本地 
def get_img(url):
    apath = os.path.join(os.path.abspath('..'),'media')
    
    img_dir = apath+'/qsbk'
    
    # 判断目录是否存在,不存在则创建
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)
        
    user_agent = 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    headers = {'User-Agent':user_agent}
    request = urllib2.Request('http:'+url,None,headers)
    u_handle = urllib2.urlopen(request)
    data = u_handle.read()
    
    # 截取url末尾的图片名称
    img_name = os.path.basename(urllib.url2pathname(url))
    with open(img_dir+'/'+img_name,'wb') as f:
        f.write(data)

        
# 简易爬取糗事百科的段子,图片地址,点赞数,评论数        
def test(page):
    myname = threading.current_thread().name
    print 'thread:',myname,'is start'
    
    # url = "https://www.qiushibaike.com/text/page/"+str(page)
    url = "https://www.qiushibaike.com/imgrank/page/"+str(page)
    try:
        # 构造请求头部
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent':user_agent}
        request = urllib2.Request(url,None,headers)
        
        # 发送请求
        u_handle = urllib2.urlopen(request)
        
        # 获取html内容
        html_str = u_handle.read()
        
        #构造文档树
        soup = BeautifulSoup(html_str)
        
        # 选择节点
        divs = soup.select('div[id="content-left"] > div ')
        for x in divs:

            content = x.select('div[class="content"]')[0].get_text().strip()
            img_url = x.select('div[class="thumb"]')[0].a.img.get('src')
            vote_num = x.select('div[class="stats"]')[0].select('span[class="stats-vote"]')[0].get_text().strip()
            comment_num = x.select('div[class="stats"]')[0].select('span[class="stats-comments"]')[0].a.get_text().strip()

            # write_to_file(content+'\n','qiushibaike.txt')
            # write_to_file(img_url+'\n\n','qiushibaike.txt')
            pic_name = os.path.basename(urllib.url2pathname('http'+img_url))
            Qsbk.objects.create(content = content,pic_name = pic_name,pic_url = img_url)
            get_img(img_url)
            
    except urllib2.HTTPError, e:
        print e.reason        
    except urllib2.URLError, e:
        print e.reason
    else:
        print 'the page：'+str(page)+'is ok'  

def pachong(request):
    threads = []
    for page in range(1, 5):
    
        # 启动多线程，每个线程分别抓取不同的页
        t = threading.Thread(target=test, args=(page,))
        threads.append(t)
        # 单进程很慢,一页接着一页抓取
        # test(page)
    for i in threads:
        i.start()
 
    for i in threads:
        i.join()
    print 'All is Done' 


def qsbk_list(request):
 
    contact_list = Qsbk.objects.all().order_by('-id')
    paginator = Paginator(contact_list, 10) # Show 10 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)  
    # 返回信息        
    return render_to_response('qsbk_list.html', {"contacts": contacts})    
# ------------------------------------爬虫代码结束-------------------------------------    