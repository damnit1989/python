# -*- coding: utf-8 -*-
#python常见问题

'a  faq module example'

__author__ = 'lmm'


print('\n'+__file__+'\n')


if __name__ == '__main__':

	import os,sys
	
	#当前目录转换为绝对路径
	print(os.path.abspath('.'))

	#如何获取命令行参数,argv的第一个元素永远是命令行执行的.py文件名。
	print(sys.argv)
	
	#如何获取当前Python命令的可执行文件路径
	print(sys.executable)
