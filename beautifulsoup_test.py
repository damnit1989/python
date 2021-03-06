#!/usr/bin/python2
# -*- coding: utf-8 -*-
# BeautifulSoup  爬虫练习

# 安装BeautifulSoup
# 方法一：easy_install beautifulsoup4
# 方法二：pip install beautifulsoup4


# Beautiful Soup支持Python标准库中的HTML解析器(html.parser),
# 还支持一些第三方的解析器(lxml,html5lib等),如果我们不安装它,则 Python 会使用 Python默认的解析器,lxml 解析器更加强大,速度更快,推荐安装


# 导入模块
from bs4 import BeautifulSoup
import urllib

# 测试html
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b><span>The Dormouse's story</span></b><b>this is a test</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# soup = BeautifulSoup(html,'lxml)
soup = BeautifulSoup(html)
print soup.name
print type(soup.head)
print soup.head.get_text()
print type(soup.head.get_text())
print '----------------'
print soup.head.string
print type(soup.head.string)
print soup.head.title.string
print type(soup.head.title.string)
# a_list = soup.select('a')
# for a in a_list:
    # print a.get_text()
# for parent in soup.head.title.string.parents:
    # print parent.name
# for tag in soup.a.next_siblings:
    # print tag
# print soup.body.parent.name
# print soup.body.parent.attrs
# print soup.title.string
# print soup.head.string
# print soup.prettify()
# print type(soup.p)

# tag 的name属性
# print soup.p.name
# print soup.p.attrs
# print soup.p['class']
# print soup.p['name']
# print soup.head.name
# print soup.head.attrs
# print soup.title.string
# print type(soup.p.string)

# print soup.a
# print soup.a.string
# if type(soup.a.string) == 'bs4.element.Comment':
    # print type(soup.a.string)
# for content in soup.p.contents:
    # print content
# for child in soup.body.children:
    # print child
# for child in soup.descendants:
    # print child
# for str in soup.stripped_strings :
    # print str

# 小小的测试
def test():
    url_handle = urllib.urlopen('https://www.python.org/events/python-events/')
    html = url_handle.read()
    soup = BeautifulSoup(html)
    lis = soup.select('ul[class="list-recent-events menu"] > li')
    for x in lis:
        print type(x)
        print '会议:',x.h3.get_text()
        print '时间:',x.p.time.get_text()
        print '内容',x.p.select('span[class="event-location"]')[0].get_text()

        
if __name__ == '__main__':
    test()

            