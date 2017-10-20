#!/usr/bin/python
# -*- coding: utf-8 -*- 
# 了解多线程的锁机制

from atexit import register
from random import randrange
import threading
import time

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

lock = threading.Lock()        
loops = (randrange(2,5) for x in xrange(randrange(3,7)))
remaining = CleanOutputSet()

def loop(nesc):
    myname = threading.current_thread().name
    # lock.acquire()
    with lock:
        remaining.add(myname)
        print '[%s] Started %s' % (time.ctime(),myname)
        # lock.release()
    time.sleep(nesc)
        # lock.acquire()
    with lock:
        remaining.remove(myname)
        print '[%s]  Completed %s (%d secs)' % (time.ctime(),myname,nesc)
        print '(remaining:%s)' % (remaining or 'NONE')
        # lock.release()
    
    
def _main():
    for pause in loops:
        threading.Thread(target=loop,args=(pause,)).start()
        
        
@register
def _atexit():
    print 'all Done at:',time.ctime()
    
    
if __name__ == '__main__':
    _main()
    
    
