# -*- coding: utf-8 -*- 

#介绍python的迭代操作

' a iteration module example'

__author__ = 'lmm'



from collections import Iterable


#判断一个数据是否可以应用迭代操作(for .. in ..)
str = "abc";
list = [1,2,3]
int = 123
tuple = (1,2,3)
dict = {'one':1,'two':2,'three':3}

print(isinstance(str,Iterable))
print(isinstance(list,Iterable))
print(isinstance(int,Iterable))
print(isinstance(tuple,Iterable))
print(isinstance(dict,Iterable))


#迭代list的键
for key in dict:
	print(key)

	
#迭代list的值	
for val in dict.values():
	print(val)
	
	
#迭代list的键和值
for k,v in dict.items():
	print(k,v)

	
#Python内置的enumerate函数可以把一个list变成索引-元素对	
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
	
	
if __name__ == '__main__':
	print(__author__)
