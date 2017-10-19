#!/usr/bin/python2
# -*- coding: utf-8 -*-
# 简易爬取百度搜索的每页标题信息  
# 本示例为在百度输入python,然后获取第一页的url地址

'''BeautifulSoup 爬虫实例2'''


from bs4 import BeautifulSoup
import urllib2, urllib


def get_soup(url):
    u_handle = urllib.urlopen(url)
    html_str = u_handle.read()
    soup = BeautifulSoup(html_str)
    return soup

    
def get_content(p):
    divs = soup.select('.c-container')
    for div in divs:
        print div.h3.a.get_text() #获取主标题
        print div.h3.a['href']  #获取a标签的href属性   
    print '第 '+str(p)+' 抓取成功\n\n' 


def init_host():
    host = "http://www.baidu.com"
    return host
    
    
if __name__ == '__main__':        
    
    host = init_host()
    url = host+ "/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=python&rsv_pq=ce9438300000923d&rsv_t=fedbt%2BPStfm7%2FHK9iCMm%2Bx2v1kXfaGRalzCgOD0NACcLXv6lSnHnqtvq1Mw&rqlang=cn&rsv_enter=1&rsv_sug3=7&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&inputT=2084&rsv_sug4=2347&rsv_sug=2"

    # 首先抓取第一页内容
    soup = get_soup(url)
    get_content(1)

    # 通过第一页来获取底部页码数据
    pages = soup.select('#page > a')
    
    # 抓取其他页数据2,3,4....10,11
    num = 2
    for page in pages:
        soup = get_soup(host+page['href'])
        get_content(num)  
        num+= 1