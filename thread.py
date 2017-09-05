#!/usr/bin/python
# -*- coding: utf-8 -*- 
#python的多线程操作

'a thread module example'

__author__ = 'lmm'


import time,threading

def loop():
	print('thread %s is running ..' % threading.current_thread().name)
	n = 0
	while n<5:
		n += 1
		print('thread %s >>> %s' % (threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s ended' % threading.current_thread().name)
	
print('thread %s is running' % threading.current_thread().name)
t = threading.Thread(target = loop,name='')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)
		
		
if __name__ == '__main__':
	print('this is a good example')
		
		
		
		
		