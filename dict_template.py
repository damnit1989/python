<<<<<<< HEAD
# -*- coding: utf-8 -*-
#字典的格式化字符串

'a  dict_str module example'

__author__ = 'lmm'


dict = {'name':'lmm','age':27,'burn':'shanxi'}
str = "please tell me you name:%(name)s" % dict
print(str)


#把字典的数据分配到模板文件中
template = '''<html>
<head>%(head)s</head>
<body>
<h1>%(title)s<h1>
<p>%(name)s</p>
</body>
'''

data = {'head':'test','title':'this is a test','name':'lmm'}
=======
# -*- coding: utf-8 -*-
#字典的格式化字符串

'a  dict_str module example'

__author__ = 'lmm'


dict = {'name':'lmm','age':27,'burn':'shanxi'}
str = "please tell me you name:%(name)s" % dict
print(str)


#把字典的数据分配到模板文件中
template = '''<html>
<head>%(head)s</head>
<body>
<h1>%(title)s<h1>
<p>%(name)s</p>
</body>
'''

data = {'head':'test','title':'this is a test','name':'lmm'}
>>>>>>> 7aeeaf3d607e377b01a1647554ed4bfd2b20463c
print(template % data)