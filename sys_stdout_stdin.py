# -*- coding: utf-8 -*-

import sys

'a sys.stdout,sys.stdin module example'


__authro__ = 'lmm'


# print 会调用 sys.stdout 的 write 方法
sys.stdout.write('hello' + '\n')
print 'hello'


# 原始的 sys.stdout 指向控制台
# 如果把文件的对象的引用赋给 sys.stdout，那么 print 调用的就是文件对象的 write 方法
__console__ = sys.stdout
f_handle = open('out.log', 'w')
sys.stdout = f_handle
print 'hello'


sys.stdout = __console__

sys.stdout.write('sdfsdf' + '\n')
