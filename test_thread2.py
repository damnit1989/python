#!/usr/bin/python
# -*- coding: utf-8 -*- 


import threading
import re
import time
import urllib2
from atexit import register

REGEX = re.compile('#([\d,]+) in Books ')
AMZN = 'http//amazon.com/dp/'

ISBNS = {
    '0132269937':'Core Python Programming',
    '0132356139':'Python Web Development with Django',
    '0137143419':'Python Fundamentail',
}

def getRanking(isbn):
    page = urllib2.urlopen('%s%s' % (AMZN,isbn))
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]
    
def _showRaning(isbn):
    print '-%r ranked  %s' %(ISBNS[isbn],getRanking(isbn))
    
    
def main():
    print 'at',time.ctime(),'on amzon...'
    for isbn in ISBNS:
        # _showRaning(isbn)
        
        #派生线程,并且立即启动
        threading.Thread(target=_showRaning,args=(isbn,)).start()
    
@register
def _atexit():
    print 'all done at:',time.ctime()
    
if __name__ == '__main__':
    pass
    main()