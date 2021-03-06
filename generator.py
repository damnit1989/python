# -*- coding: utf-8 -*- 
#python生成器实例
#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了


'a generator module example'

__author__ = 'lmm'



#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

#列表生成式
list = [x for x in range(1,10) if x%2 == 0]
print(list)

#generator
G1 = (x for x in range(1,10))
print(type(G1))	#<type 'generator'>
print(G1)	#<generator object <genexpr> at 0x000000000255E2D0>	


#判断G1是否可迭代
from collections import Iterable
print(isinstance(G1,Iterable))
print(next(G1))


#斐波拉契数列
def fib(max):
	n,a,b = 0,0,1
	while n<max:
		a,b = b,a+b #t = (b, a + b) # t是一个tuple a = t[0] b = t[1]
		print(b)		
		n+= 1
	return 'done'
fib(5)


          # 1
        # 1   1
      # 1   2   1
    # 1   3   3   1
  # 1   4   6   4   1
# 1   5   10  10  5   1

#定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
#杨辉三角	
def triangles(lines):
    L = [1]
    n = 1
    yield L
    while n < lines:
		n = n + 1
		nL = [1]
		for i in range(1,n-1):
			nL.append(L[i - 1] + L[i])

		nL.append(1)
		L = nL
		yield nL

for t in triangles(10):
    print(t)
	
	
	
def fib_yie(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n += 1
	# return 'done'

	
	
if __name__ =='__main__':
	for x in fib_yie(10):
		print(x)