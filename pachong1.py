#!/usr/bin/python2
# -*- coding: utf-8 -*-
# 简易爬取糗事百科的段子,图片地址,点赞数,评论数  

'''BeautifulSoup 爬虫实例1'''


import urllib, urllib2
from bs4 import BeautifulSoup
import os
#from lxml import etree


# 写入文件
def write_to_file(content,filename):
    with open(filename,'a') as f:
        f.write(content.encode('utf-8'))

        
# 获取图片保存到本地 
def get_img(url):
    apath = os.path.abspath('.')
    img_dir = apath+'/jsbk'
    
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
            # data = {}
            # data['内容'] = x.select('div[class="content"]')[0].get_text().strip()
            # data['图片地址：'] = x.select('div[class="thumb"]')[0].a.img.get('src')
            # data['好笑：'] = x.select('div[class="stats"]')[0].select('span[class="stats-vote"]')[0].get_text().strip()
            # data['评论：'] = x.select('div[class="stats"]')[0].select('span[class="stats-comments"]')[0].a.get_text().strip()
            # print data
            
            content = x.select('div[class="content"]')[0].get_text().strip()
            img_url = x.select('div[class="thumb"]')[0].a.img.get('src')
            vote_num = x.select('div[class="stats"]')[0].select('span[class="stats-vote"]')[0].get_text().strip()
            comment_num = x.select('div[class="stats"]')[0].select('span[class="stats-comments"]')[0].a.get_text().strip()

            write_to_file(content+'\n','qiushibaike.txt')
            write_to_file(img_url+'\n\n','qiushibaike.txt')
            get_img(img_url)
            
    except urllib2.HTTPError, e:
        print e.reason        
    except urllib2.URLError, e:
        print e.reason
    else:
        print 'the page：'+str(page)+'is ok'
        

if __name__ == '__main__':
    for page in range(1, 5):
        test(page)
