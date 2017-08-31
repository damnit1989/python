# -*- coding: utf-8 -*-

' a test module '

__author__ = 'lmm'
import sys

def test():
	args = sys.argv
	print(args[0],args[1],args[2])
	num = len(args)
	print(num)
	print(__name__)
	
#当我们在命令行运行该模块文件时，Python解释器把一个特殊变量__name__置为__main__	
if __name__ == '__main__':
	test()
	# print(__name__)