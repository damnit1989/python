# -*- coding: utf-8 -*-
#python的继承和多态

'a sub_base class module example'

__author__ = 'lmm'


#父类
class Animal(object):
	def run(self):
		print("animal is running!")
		# pass

#子类
class Dog(Animal):
	def run(self):
		print('dog is running!')
	# pass
	
class Cat(Animal):
	def run(self):
		print('cat is running')
	# pass
	
dog = Dog()
cat = Cat()
dog.run()
cat.run()
#dog和cat都是Animal数据类型
print(isinstance(dog,Animal))
print(isinstance(cat,Animal))


#为什么下面这种打印方式会多打印一个'none'? 暂时不解
# print(Dog().run())
# print(Cat().run())


#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

#Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个run()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了run()方法的对象
class Person(object):
	def run(self):
		print('person is running!')
		# pass

def run_type(x):
	x.run()
	
run_type(Animal())
run_type(Dog())
run_type(Cat())
run_type(Person())


if __name__ == '__main__':
	print("end")
