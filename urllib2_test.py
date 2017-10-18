#!/usr/bin/python2
# -*- coding: utf-8 -*-
# urllib2 请求url

import urllib,urllib2
 
url = 'https://passport.csdn.net/account/login?service=http://www.csdn.net'
values = {
    'username':'bitch1989',
    'password':'lmm-3971655',
    'lt':'LT-112837-tVUFaIwIgPEJOkGtyPxZ3tI6Za95fF',
    'execution':'e1s1',
    '_eventId':'submit',
    }
headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                        'Referer':'http://www.csdn.net' } 
data = urllib.urlencode(values)
url += '?' + data

url = 'http://www.xxxxx.com/'
request = urllib2.Request(url,None,headers)
try:
    # 增加调试信息
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler, httpsHandler)
    urllib2.install_opener(opener)

    ret = urllib2.urlopen(request)
    # print ret.read()
except urllib2.HTTPError, e:
    print '子类异常'
    print e.reason
    print '子类异常'
except urllib2.URLError, e:
    print'aaaaaaaaaaaaaaaaaa'
    print e.reason
    print 'bbbbbbbbbbbbbbbbb'
    # print e.code
else:
    print 'ok'


if __name__ == '__main__':
    import urllib2
    import cookielib
    #声明一个CookieJar对象实例来保存cookie
    cookie = cookielib.CookieJar()
    #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler=urllib2.HTTPCookieProcessor(cookie)
    #通过handler来构建opener
    opener = urllib2.build_opener(handler)
    #此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print 'Name = '+item.name
        print 'Value = '+item.value
