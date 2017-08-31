# -*- coding: utf-8 -*- 

#python字典格式
dic = {'name':'lmm','age':25,'set':'man'}
print(dic['set'])


#定义函数
def num(x):
	if x > 8:
		print "大于8"
	else:
		print "小于8"
	
num(4)



#定义类
class Student(object):

	def __init__(self,name,score):
		self.name = name
		self.score = score
	def getName(self):
		return self.__name
	def getScore(self):
		return self.__score
student = Student('lmm',10)
# print student.getName()
# print student.getScore()
# student.__score = 1
print student.score
print type(student)


class Class(object):
    name = "jack"
    def __init__(self):
        self.name = 'alice'

instance = Class()
print Class.name #jack
# del Class.name   可以删除类属性，也可以删除实例属性
print instance.name #alice
print Class.name #AttributeError: type object #Class' has no attribute 'name'


from datetime import datetime
now = datetime.now() # 获取当前datetime 
print(now)
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)


import pdb

# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接:
s.connect(('localhost', 80))

# 模拟get发送数据:
# s.send(b'GET /lmm/test.php HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n')


#模拟post发送数据

str = ("POST /lmm/test.php HTTP/1.1\r\n"
        "Host: localhost\r\n"
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
        # "Referer: http://www.xxxxx.com/\r\n"
        "Content-Length: 17\r\n"
        "Cookie: session=f28edeacd71e759d05a80bb3cd9c91856952b3e3%7E58eb987a9efb26-19897462\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        "Connection: keep-alive\r\n\r\n"
        "param1=a&param2=b"
	)
s.send(str)	


# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(2048)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接:
s.close()

# 打印数据
print(data)



#python 读写文件操作

#读打开文件
# f = open("open.txt",'r') 

#写打开文件
# f = open("open.txt",'w') 

#读取文件内容到内存
# content = f.read()

#写内容到文件
# str = "this is a test content to write to txt file"
# f.write(str)
# f.close();

#简化版读操作
# with open('open.txt','r') as f:
	# print(f.read())
	
# #简化版写操作
# with open('open.txt','w') as f:
	# str = "continue write content to file"
	# print(f.write(str))
	
#逐行读取文件内容	
with open('open.txt','r') as f:
	for line in f.readlines():
		pdb.set_trace()#打断点
		print(line)
		
		
#json字符串与字典格式的转化
import json
dic = {"name":"lmm","age":25,"set":"man"}
print(type(dic))
print(type(json.dumps(dic)))

dic = dict(one = 1,two = 12,three = 'three')
print(json.dumps(dic))
print(type(dic))

json_str = '{"name":"wo","height":123,"weight":60}';
dic = json.loads(json_str)
print(dic['name'])		



