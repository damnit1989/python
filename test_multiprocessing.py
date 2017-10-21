#!/usr/bin/python
# -*- coding: utf-8 -*- 
# 学习python多进程，到底还是不知道讲些神马


import multiprocessing
import time
import os, sys
# def process(num):
    # time.sleep(num)
    # print 'process:%d' % num
    

    
class MyProcess(multiprocessing.Process):
    def __init__(self,loop, lock):
        multiprocessing.Process.__init__(self)
        self.loop = loop
        self.lock = lock
    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print 'Pid: ' + str(self.pid) + ' LoopCount: ' + str(count)

            
# 直接退出程序            
# os._exit(0)
# sys.exit()
if __name__ == '__main__':
    
    # for i in range(1,5):
        # p = multiprocessing.Process(target=process,args=(i,))
        # p.start()
    # print 'CPU number:' + str(multiprocessing.cpu_count())
    
    # for p in multiprocessing.active_children():
        # print 'Child process name:' + p.name + ' id :' + str(p.pid)
		
	# print 'Process Ended'	
    
    for i  in range(10,15):
        lock = multiprocessing.Lock()
        p = MyProcess(i, lock)
        p.deamon = True
        p.start()
        # p.join()
    print 'Main process Ended'
    os._exit(0)
    # os._exit(1)
    # try:
        # sys.exit(0)
    # except:
        # print 'die'
		
		
		