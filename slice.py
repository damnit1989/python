# -*- coding: utf-8 -*- 
#list，tuple，str切片实例

' a slice module '

__author__ = 'lmm'

#list数据类型的切片
list = range(1,101)
print(list[::2])
print(list[:10:1])

#tuple数据类型的切片
tuple = tuple(range(1,10))
print(tuple[::2])
print(tuple[:10:1])
print(tuple[:])

#str数据类型的切片
#Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。
str = 'abcdefg'
print(str[:3])
print(str[::2])

