#!/usr/bin/python2
# -*- coding: utf-8 -*-
# urllib 请求url

'''
Python的urllib和urllib2模块都做与请求URL相关的操作,但他们提供不同的功能.他们两个最显着的差异如下:
    urllib2可以接受一个Request对象,并以此可以来设置一个URL的headers,但是urllib只接收一个URL.这意味着,你不能伪装你的用户代理字符串等.
    urllib模块可以提供进行urlencode的方法，该方法用于GET查询字符串的生成，urllib2的不具有这样的功能。这就是urllib与urllib2经常在一起使用的原因
'''

import urllib, urllib2
import json


__author__ = 'lmm'


# with urllib.urlopen('https://api.douban.com/v2/book/2129650') as f:

url = 'https://api.douban.com/v2/book/2129650'

# urlopen方法调用
# f = urllib.urlopen(url)
# data = f.read()
# dict_data = json.loads(data)
# for k,v in dict_data.items():
    # print k,'==',v
# print('Status:', f.getcode(), f.geturl())
# f.close()


# # urlretrieve方法调用,返回内容存入本地文件
# filename,headers = urllib.urlretrieve(url,'lmm.txt')
# print '存入本地文件:',filename
# print '返回请求头部:'
# headers_dict = dict(headers);
# for k, v in headers_dict.items():
    # print '【'+k+'】',':',v


class UrllibTest():
    url = 'https://api.douban.com/v2/book/2129650'
    
    def __init__(self,url):
        self.url = url
        
    # urlopen方法调用
    @staticmethod
    def testUrlOpen():
        f_handle = urllib.urlopen(url)
        data = f_handle.read()
        dict_data = json.loads(data)
        for k,v in dict_data.items():
            print k,'==',v
        print('Status:', f_handle.getcode(), f_handle.geturl())
        f_handle.close()

    # urlretrieve方法调用,返回内容存入本地文件
    @classmethod
    def testUrlRieve(cls,localfile):
        filename,headers = urllib.urlretrieve(cls.url,localfile)
        print '存入本地文件:',filename
        print '返回请求头部:'
        headers_dict = dict(headers);
        for k, v in headers_dict.items():
            print '【'+k+'】',':',v        


# 重点问题，类的所属方法和类的静态方法，既可以被类本身调用，也可以被类的实例调用
# 这个貌似很个性啊            
obj = UrllibTest(url)
obj.testUrlRieve('test.txt')
obj.testUrlOpen()

UrllibTest.testUrlOpen()
UrllibTest.testUrlRieve('test.txt')


# get方式请求
# import urllib
# params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# f = urllib.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)
# print f.read()

# post方式请求
# import urllib
# params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# f = urllib.urlopen("http://www.musi-cal.com/cgi-bin/query", params)
# print f.read()


# urllib2示例
# url = 'http://www.someserver.com/cgi-bin/register.cgi'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {'name' : 'Michael Foord',
          # 'location' : 'Northampton',
          # 'language' : 'Python' }
# headers = { 'User-Agent' : user_agent }
# data = urllib.urlencode(values)
# req = urllib2.Request(url, data, headers)
# response = urllib2.urlopen(req)
# the_page = response.read()