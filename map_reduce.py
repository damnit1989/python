# -*- coding: utf-8 -*-
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是:
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


'a how to use map(),reduce() module example'


__author__ = 'lmm'


L = [1, 2, 3, 4, 5]
new_l = map(str, L)
print new_l


def test(x):
    return x*x

print map(test, L)


def chr_func(x):
    return x+'_'+x

print map(chr_func, 'abcdef')


from functools import reduce
def fn(x,y):
    return x*10 + y

print(reduce(fn,[1,3,5,7,9]))
