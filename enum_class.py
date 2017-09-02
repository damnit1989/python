# -*- coding: utf-8 -*-
#python枚举类

'a enum module example'

__author__ = 'lmm'


from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)