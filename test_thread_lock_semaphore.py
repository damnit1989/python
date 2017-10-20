#!/usr/bin/python
# -*- coding: utf-8 -*- 
# 了解多线程的锁，信号量


from atexit import register
from random import randrange
import threading
import time

lock = threading.Lock()
MAX = 5
candytray = threading.BoundedSemaphore(MAX)

def refill():
    with lock:
        print 'Refilling candy...'
        try:
            candytray.release()
        except ValueError:
            print 'full,skipping'
        else:
            print 'ok'
        
def buy():
    with lock:
        print 'buying candy...'
        if candytray.acquire(False):
            print 'ok'
        else:
            print 'empty,skipping'
        
def producer(loops):
    for i in xrange(loops):
        refill()
        time.sleep(randrange(3))
        
def consumer(loops):
    for i in xrange(loops):
        buy()
        time.sleep(randrange(3))
        
def _main():
    print 'starting at:',time.ctime()
    nloops = randrange(2,6)
    print 'THE CANDY MATCH (full with %d bars)!' % MAX
    threading.Thread(target=consumer,args=(randrange(nloops,nloops+MAX+2),)).start()
    # threading.Thread(target=producer,args=(nloops,)).start()
    
    
@register
def _atexit():
    print 'all DOne at:',time.ctime()
    
    
if __name__ == '__main__':
    _main()
    
