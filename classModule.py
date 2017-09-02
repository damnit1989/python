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

#在一个实例里， __girl表示“我是贞女，你不能上我”
# _girl表示“你虽然可以上我，但你应该把我看做贞女” 
#girl表示“我是荡妇，谁都可以上我” 但是python仍然可以用_类名__girl强上贞女
print(a._TestImport__name)



if __name__ == '__main__':
	pass