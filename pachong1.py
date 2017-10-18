#!/usr/bin/python2
# -*- coding: utf-8 -*-
# 爬虫实例1


import urllib, urllib2
from lxml import etree
page = 1
url = "https://www.qiushibaike.com/hot/page/"+str(page)

try:
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent':user_agent}
    request = urllib2.Request(url,None,headers)
    u_handle = urllib2.urlopen(request)
    ret = u_handle.read()

    html = etree.HTML(ret)
    nodes = html.xpath('//div[@id="content-left"]/div')
    for node in nodes:
        print node.xpath('a/div/span/text()')
    print len(nodes)    
except urllib2.HTTPError, e:
    print 'http请求 错误'
    print e.reason
except urllib2.URLError, e:
    print 'url地址错误'
    print e
except Exception, e:
    print e
    print 'no '
else:
    print 'ok'
    # print ret