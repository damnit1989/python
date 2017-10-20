#!/usr/bin/python
# -*- coding: utf-8 -*- 
# 线程1在4秒后退出，线程2在两秒后退出
import threading 
import time

loops = [4,2]

# def loop(nloop,nsec):
    # print 'start loop',nloop,'at:',time.ctime()
    # time.sleep(nsec)
    # print 'loop',nloop,'done at',time.ctime()
    
# def main():
    # print 'starting  at:',time.ctime()
    # threads = []
    # nloops = range(len(loops))
    # for i in nloops:
        # t = threading.Thread(target=loop,args=(i,loops[i]))
        # threads.append(t)
        
    # for i in nloops:
        # threads[i].start()
    # for i in nloops:
        # threads[i].join()
        
    # print 'all Done at:',time.ctime()
    
    
class ThreadFunc(object):
    def __init__(self,func,args,name = ''):
        self.name = name
        self.func = func
        self.args = args
    #对象通过提供__call__(slef, [,*args [,**kwargs]])方法可以模拟函数的行为，如果一个对象x提供了该方法，就可以像函数一样使用它，也就是说x(arg1, arg2...) 等同于调用x.__call__(self, arg1, arg2) 
    def __call__(self):
        self.func(*self.args)
        
def loop(nloop,nsec):
    print 'start loop',nloop,'at:',time.ctime()
    time.sleep(nsec)
    print 'loop',nloop,'done at:',time.ctime()
    
def main():
    print 'starting at:',time.ctime()
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target = ThreadFunc(loop,(i,loops[i]),loop.__name__))
        threads.append(t)
        
    for i in nloops:
        threads[i].start()
        
    for i in nloops:
        # join()方法是阻塞的，在所有的子线程执行完后才会执行主线程
        threads[i].join()
        
    
    print 'all Done at:',time.ctime()
if __name__ == '__main__':
    main()
    
    
    
    # 单线程模式
    # def loop0():
        # print 'start loop0 at:',time.ctime()
        # time.sleep(4)
        # print 'loop0 done at',time.ctime()
    # def loop1():
        # print 'start loop1 at:',time.ctime()
        # time.sleep(2)
        # print 'loop1 done at',time.ctime()
    # print 'starting at:',time.ctime()
    # loop0()
    # loop1()
    # print 'all Done at:',time.ctime()