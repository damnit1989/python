# -*- coding: utf-8 -*-
#读取配置文件conf.cgf

'''
read conf example,you can use the __doc__  print out the infomation
please just do  it

'''

__author__ = 'lmm'

from ConfigParser import ConfigParser
import time 

conf_file = 'conf.cfg'
conf = ConfigParser()
conf.read(conf_file)

print conf.get('info','name'),conf.get('info','age')

time .sleep(3)

print conf.get('addr','born')
print conf.get('addr','city')
