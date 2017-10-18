# -*- coding: utf-8 -*-
import urllib
from lxml import etree


# url = 'https://www.python.org/events/python-events/'
# f_handle = urllib.urlopen(url)
# data = f_handle.read()
# html = etree.HTML(data)
# nodes = html.xpath('//ul[@class="list-recent-events menu"]/li')
# for node in nodes:
    # time = node.xpath('p/time/text()')
    # zt = node.xpath('h3[@class="event-title"]/a/text()')
    # address = node.xpath('p/span[@class="event-location"]/text()')
    
    # data = {'time':time,'zt':zt,'address':address}
    # print data
    

# url = 'https://docs.python.org/3/faq/'
# fHandle = urllib.urlopen(url)
# result = fHandle.read()
# html = etree.HTML(result)
# nodes = html.xpath('//div[@class="toctree-wrapper compound"]/ul/li')
# L = []
# for node in nodes:
    # L.append(node.xpath('a/text()')[0])
# print L


url = "http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=a&rsv_"
fhandle = urllib.urlopen(url)
result = fhandle.read()
html = etree.HTML(result)
nodes = html.xpath('//div[@id="content_left"]/div')
for node in nodes:
    print node.xpath('h3/a/text()')
print len(nodes)