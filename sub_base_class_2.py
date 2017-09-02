# -*- coding: utf-8 -*-
#python的继承和多态2

'another sub-base module example'

__author__ = 'lmm'


#基类
class Animal(object):
	def run(self):
		print("animal is running")
	def run_type(self):
		print(self.run())
	def run_type_base(self,Animal):
		print(self.run())
		print(Animal.run())


class Dog(Animal):
	def run(self):
		print('dog is running')
class Cat(Animal):
	def run(self):
		print('cat is running')


if __name__ =='__main__':
	animal = Animal()
	animal.run_type_base(Dog())
	dog = Dog()
	dog.run_type()
	print(dir())
