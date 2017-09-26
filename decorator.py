# -*- coding: utf-8 -*-
# 装饰器
# 编写高阶函数，就是让函数的参数能够接收别的函数


'a decorator module example for test'
''' this is the detail description '''


__author__ = 'lmm'


# 定义装饰器
def dec(func):
    def wark(*agrs, **kw):
        print 'this call %s' % func.__name__
        return func(*agrs, **kw)
    return wark


@dec
def test():
    print 'this is test function'


# 高阶函数
# 函数的返回值是一个函数
def high_func(*args):
    def total():
        sum = 0
        for i in args:
            sum += i
        return sum
    return total


if __name__ == '__main__':
    test()
    f = high_func(1, 2, 3, 4, 5)
    print f
    print f()
