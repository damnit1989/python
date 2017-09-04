#!/usr/bin/python
# -*- coding: utf-8 -*- 

'a muti_process moduel example'

__author__ = 'lmm'

import os

print("process %s start .." % os.getpid())
pid = os.fork()
if pid == 0:
	print('i am child process %s and my parent is %s' %(os.getpid(),os.getppid()))
else:
	print('I %s just created a child process %s '%(os.getpid(),pid))