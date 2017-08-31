# -*- coding: utf-8 -*- 
from file import *
import pdb


fromFile = 'open.txt'
toFile = 'write.txt'

# inStr = input('please input your file name:')
# toFile = inStr+'.txt'
# print(toFile)
# readFile(fromFile,toFile)

test_list()

#调用可变参数
list = [1,2,3,4]
# tup = (1,2)
# name = input('姓名:')
# age = input('年龄:')
# height = input('身高:')
# list = [name,age,height]
print(changeArg(*list))

#调用关键字参数
dict = {'height':180}
persion('lmm',18,**dict)

# pdb.set_trace()#打断点

print(recur(3))

l = []
n = 1
while n<=10:

	l.append(n)
	n += 1
	
print(type(l))