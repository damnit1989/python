<<<<<<< HEAD
# -*- coding: utf-8 -*-


class Student(object):
	# name = ''
	# number = ''
	def __init__(self,name='a',number = '123456'):
		self.name = name
		self.number = number
	def test(self,*argu):
		sum = 0
		for i in argu:
			print(i)
			sum += i
		print(sum)
		self.getStudentInfo()
	def getStudentInfo(self):
		print(self.name,self.number)
	

if __name__ == '__main__':
	import sys
	args = sys.argv
	num = range(1,10)
	# del(Student.name)		
	student = Student('lmm','654321')
	student.test(*num)

	# student.getStudentInfo()
	print(Student)

	print(student.name)
=======
# -*- coding: utf-8 -*-


class Student(object):
	# name = ''
	# number = ''
	def __init__(self,name='a',number = '123456'):
		self.name = name
		self.number = number
	def test(self,*argu):
		sum = 0
		for i in argu:
			print(i)
			sum += i
		print(sum)
		self.getStudentInfo()
	def getStudentInfo(self):
		print(self.name,self.number)
	

if __name__ == '__main__':
	import sys
	args = sys.argv
	num = range(1,10)
	# del(Student.name)		
	student = Student('lmm','654321')
	student.test(*num)

	# student.getStudentInfo()
	print(Student)

	print(student.name)
>>>>>>> 7aeeaf3d607e377b01a1647554ed4bfd2b20463c
	print(args[1])