# -*- coding: utf-8 -*- 
#列表生成式
'a list module example'

__author__ = 'lmm'

list = range(1,10)
print(type(list))
print(list)

list = [x for x in range(1,10)]
print(list)


#列表生成式，筛选出字符串，并且转成小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
L3 = [x for x in L1 if isinstance(x,int)]
print(L2)
print(L3)


#列表生成式同时可以有多个for循环
L1 = ('Hello', 'World', 'bb', 'Apple', 'aa')
L2 = ('Hello', 'World', 'bb', 'Apple', 'aa')
L3 = [x+'='+y for x in L1 for y in L2 if x != y]
print(L3)

L1 = "ABC"
L2 = "ABC"
L3 = [x+y for x in L1 for y in L2 if x != y]
print(L3)


if __name__ == '__main__':
	L1 = [x for x in range(1,10) if x%2 != 0]
	print(L1)
	print(__name__)

