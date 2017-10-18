#!/usr/bin/python2
# -*- coding: utf-8 -*-
# BeautifulSoup

from bs4 import BeautifulSoup
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
# soup = BeautifulSoup(html)
soup = BeautifulSoup(html,'lxml')

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
if __name__ == '__main__':
    # pass
    import urllib
    url_handle = urllib.urlopen('https://www.python.org/events/python-events/')
    html = url_handle.read()
    soup = BeautifulSoup(html,'lxml')
    lis = soup.select('ul[class="list-recent-events menu"] > li')
    for x in lis:
        print type(x)
        print '会议:',x.h3.get_text()
        print '时间:',x.p.time.get_text()
        print '内容:',x.p.span.get_text()


            