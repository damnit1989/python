# -*- coding: utf-8 -*- 
#可变数据类型，当赋值给另一个变量时，其实是做了一次引用，两个变量指向同一对象
a = {'one':1,'two':2}
b = a
b['three'] = 3
print(b,a)


c = ['one','two']
d = c
d.append('three')
print(d,c)

str = '-'
str = ''.join(c)
print(str)
