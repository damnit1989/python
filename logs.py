# -*- coding: utf-8 -*-

' a test module '

__author__ = 'lmm'

import os
from time import strftime

logsdir = '/var/log/mysql'
zip_commend = 'zip'

for files in os.listdir(logsdir):
    print(files)
    if files.endswith('.log'):
        files1 = files +'.'+strftime('%Y-%m-%d') + '.zip'
        os.chdir(logsdir)
        os.system(zip_commend + ' ' + files1 + ' ' + files)

        
        
        
        
        