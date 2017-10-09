# -*- coding: utf-8 -*-
# 类对象的迭代器
# 生成器示例
# 将迭代器转换成list


' a super function test module '


__author__ = 'lmm'

# class Fibs:
    # def __init__(self):
        # self.a = 0
        # self.b = 1
    # def next(self):
        # self.a,self.b,self.a+self.b
    # def __iter__(self):
        # return self
        
# fibs = Fibs()
# for f in fibs:
    # if f > 10:
        # print f
        # break

def func(nested):
    for sublist in nested:
        for ele in sublist:
            # print ele
            yield ele

L = [[1,2],[3,4],[5]]
func(L)


def ood():
    print 'step 1'
    yield (1)
    print 'step 2'
    yield (2)
    print 'step 3'
    yield (3)
    
d = ood()
for i in d:
    print i
# next(d)
# next(d)
# next(d)


# 将迭代器转换成list
class TestIter:
    val = 0
    def next(self):
        self.val += 1
        if self.val > 10:
            raise StopIteration
        return self.val
    def __iter__(self):
        return self
test_iter = TestIter()
a = list(test_iter)
print a
