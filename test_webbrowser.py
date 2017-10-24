# -*- coding: utf-8 -*- 


import webbrowser
import sys
import os
import socket
import urllib


def test_webbrowser(list = None):
    if list is not None:
        for url in list:
            webbrowser.open(url)

    else:
        print 'the url_list is empty'


def get_public_ip():
    read_res = urllib.urlopen('http://ipecho.net/plain').read()
    return read_res.encode('utf-8')


def get_local_ip():
    local_ip = socket.gethostbyname(socket.gethostname())
    return local_ip


if __name__ == '__main__':
    url_list = [
		'http://www.baidu.com',
		'http://qiushibaike.com'
	]

    test_webbrowser(url_list)

    print 'Geting Public ip and local ip ...'
    print 'Public ip is %s and  local ip is %s' %(get_public_ip(), get_local_ip())