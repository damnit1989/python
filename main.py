# -*- coding: utf-8 -*-

' a test module '

__author__ = 'lmm'

# import module
# from ../module import test
import sys
sys.path.append("..") #从上级目录导入模块
from module import test
test()

if __name__ == '__main__':
	print('this is main')
	pass
	# test()
	# print(__name__)