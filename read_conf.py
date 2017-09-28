# -*- coding: utf-8 -*-
#读取配置文件conf.cgf

'read conf example'

__author__ = 'lmm'

from ConfigParser import ConfigParser

conf_file = 'conf.cfg'
conf = ConfigParser()
conf.read(conf_file)

print conf.get('info','name'),conf.get('info','age')

print conf.get('addr','born')