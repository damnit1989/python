#!/usr/bin/python2
# -*- coding: utf-8 -*-
# bitch，shit


from bs4 import BeautifulSoup
import urllib, urllib2
from lxml import etree
import os


def request_url(url):
    headers = {'User-Agent':user_agent,}
    request = urllib2.Request(url,None,headers)
    u_handle = urllib2.urlopen(request)
    html_str = u_handle.read()
    return html_str

    
def get_content(p):
    videos = soup.select('div[class="content"] .img')
    for video in videos:
        print url+video['src']
        get_img(url+video['src'])  
    print '第 '+str(p)+' 页抓取成功\n\n'

    

def get_img(url):
    apath = os.path.abspath('.')
    img_dir = apath+'/bitch'
    
    # 判断目录是否存在,不存在则创建
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)
    
    data = request_url(url)
    
    # 截取url末尾的图片名称
    img_name = os.path.basename(urllib.url2pathname(url))
    with open(img_dir+'/'+img_name,'wb') as f:
        f.write(data)

# url = "http://www.69sexvideos.com"
try:
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'

    html_data = request_url(url)
    soup = BeautifulSoup(html_data)
    get_content(1)
    
    pages = soup.select('#pagination a')
    num = 2
    for page in pages:
        data = request_url(url+page['href']) 
        soup = BeautifulSoup(data)        
        get_content(num)
        num += 1

except urllib2.HTTPError, e:
    print e.reason        
except urllib2.URLError, e:
    print e.reason
else:
    print 'ok'