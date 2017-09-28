# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from .models import Test,article
 
# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

def testArticleDb(request):
    # insert_data = {'title':'2222','text':'4444444444444','create_date':'2017-09-22 11:41:48'}
    # insert_data = (title='2222',text='4444444444444',create_date='2017-09-22 11:41:48')
    # insert_data = "(title='2222',text='4444444444444',create_date='2017-09-22 11:41:48')"
    # article1 = article(insert_data)
    article1 = article(title='wwwwwwwwwww',text='xxxxxxxxxxxxxxxx',create_date='2017-09-22 11:41:48')
    article1.publish()
    str = article1.__str__()
    
    # return HttpResponse("<p>数据添加成功！</p>")    
    return HttpResponse(str)    