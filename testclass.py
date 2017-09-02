# -*- coding: utf-8 -*-
#python的类和实例

' a class module '

__author__ = 'lmm'


#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

class TestImport(object):

	def __init__(self,name='lmm',age = 20):
		self.__name = name
		self.__age = age
		self.all = [name,age]
	def getName(self):
		print("your name is %s" % (self.__name))
	def getAge(self):
		print("your age is %d" % (self.__age))
# a = TestImport()

