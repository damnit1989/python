# -*- coding: utf-8 -*-

' a class module '

# from testclass import TestImport

import testclass
a = testclass.TestImport().getName
a()


import testclass
a = testclass.TestImport()
a.getName()


if __name__ == '__main__':
	pass
	print('good')