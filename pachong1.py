#!/usr/bin/python2
# -*- coding: utf-8 -*-
# 爬虫实例1


import urllib, urllib2
#from lxml import etree
page = 1
url = "https://www.qiushibaike.com/hot/page/"+str(page)

try:
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent':user_agent}
    request = urllib2.Request(url,None,headers)
    u_handle = urllib2.urlopen(request)
    ret = u_handle.read()

    #html = etree.HTML(ret)
    #nodes = html.xpath('//div[@id="content-left"]/div')
    #for node in nodes:
    #    print node.xpath('a/div/span/text()')
    #print len(nodes)
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




if __name__ == '__main__':
    import urllib, urllib2
    from bs4 import BeautifulSoup
    page = 1
    url = "https://www.qiushibaike.com/text/page/"+str(page)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent':user_agent}
    request = urllib2.Request(url,None,headers)
    u_handle = urllib2.urlopen(request)
    html_str = u_handle.read()
    soup = BeautifulSoup(html_str)
    divs = soup.select('div[id="content-left"] > div ')
    for x in divs:
        #print type(x)
        #print x

        print '内容：',x.select('div[class="content"]')[0].get_text().strip()
        print '好笑：',x.select('div[class="stats"]')[0].select('span[class="stats-vote"]')[0].get_text()
        print '评论：',x.select('div[class="stats"]')[0].select('span[class="stats-comments"]')[0].a.get_text()