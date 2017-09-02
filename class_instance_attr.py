# -*- coding: utf-8 -*-
#python的类和实例属性

'a class or instance module example'

__author__ = 'lmm'

class Person(object):
	name = 'lmm'
	def __init__(self,age,height,name):
		self.age = age
		self.height = height
		self.name = name
		name = name



if __name__ == '__main__':
	person = Person(21,'153','liudao')
	print(person.age)
	print(person.name)
	# del(person.name)
	# print(person.name)
	print(Person.name)