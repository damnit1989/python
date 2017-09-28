#!/usr/bin/python
# -*- coding: utf-8 -*- 

'a muti_process moduel example'

__author__ = 'lmm'

import os

# print("process %s start .." % os.getpid())
# pid = os.fork()
# if pid == 0:
	# print('i am child process %s and my parent is %s' %(os.getpid(),os.getppid()))
# else:
	# print('I %s just created a child process %s '%(os.getpid(),pid))
	


from multiprocessing import Pool
import os,time,random

def long_time_task(name):
	print("Run task %s (%s)" % (name,os.getpid()))
	start = time.time()
	time.sleep(random.random()*10)
	end = time.time()
	print("Task %s runs %0.2f seconds" % (name,(end-start)))
	
if __name__ == '__main__':
	print("Parent process %s" % (os.getpid()))
	p = Pool(10)
	for i in range(10):
		p.apply_async(long_time_task,args = (i,))
	print("Waiting for all subprocess done")
	p.close()
	p.join()
	print("all subprocesses done")
		
		
		
		
		
		
		
		
		
		
		
		
		