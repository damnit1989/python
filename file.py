# -*- coding: utf-8 -*- 
' a file module example'
def readFile(fromFile,toFile):
	#python2.x版本不支持encoding参数
	# with open(fromFile,'r',encoding="UTF-8") as f: 
	with open(fromFile,'r') as f:
		# content = f.read()
		for line  in f.readlines():
			writeFile(toFile,line)
		

def writeFile(fileName,content):
	# with open(fileName,'a',encoding="UTF-8") as op:
	with open(fileName,'a') as op:
		op.write(content)
		

def test_list(L = []):
	L.append('END')
	print(L)
# def test_list(L = None):
	# L.append('END')
	# print(L)	
# test_list([1,2,3])
# test_list()

#在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
#在函数内部，参数numbers接收到的是一个tuple
#调用可变参数
def changeArg(*nums):
	print(type(nums))
	sum = 0
	for i in nums:
		sum += i*i
	return sum

#关键字参数
def persion(name,age,**arg):
	print('name:',name,'age:',age,'other:',arg)

	
#递归函数
def recur(n):
	if n == 1:
		return 1
	return n*recur(n-1)