# -*- coding: utf-8 -*- 
#操作sqlie数据库
import sqlite3
import json
import sys
import platform
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from lmm order by id desc')
values = cursor.fetchall()
#cursor.execute('insert into lmm values(3,"cc")')

#关闭连接
cursor.close()
conn.close()


def showData(val):
	for i in val:
		print(type(i))
		print(json.dumps(i))
		print(type(json.dumps(i)))


		
if __name__ == '__main__':
	platform = platform.platform()
	if 'Windows' in platform:
		print(platform)
		
	print(__name__)
	print(sys.argv)
	showData(values)

#python操作mysql数据库的方式与sqlite基本大同小异