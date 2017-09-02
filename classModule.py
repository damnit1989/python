# -*- coding: utf-8 -*-

' a class module '

__author__ = 'lmm'



#第一种导入模块方法
from testclass import TestImport
a = TestImport()
a.getName()


#第二种导入模块方法
import testclass
a = testclass.TestImport().getName
a()


#第三种导入模块方法
import testclass
a = testclass.TestImport('liudao',30)
a.getName()
print(a.all)

#双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_TestImport__name，所以，仍然可以通过_TestImport__name来访问__name私有变量：
print(a._TestImport__name)



if __name__ == '__main__':
	pass