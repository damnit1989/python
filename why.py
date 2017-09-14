#!/usr/bin/python
# -*- coding: utf-8 -*- 


def show():
    print 'wow~'

def ret():
    return '123'

class CLASS(object):
    x = None
    y = True
    z = show()
    w = ret()
    def __init__(self):
        self.x = 'x'

        
print(CLASS.x,CLASS.y,CLASS.z,CLASS.w)     
        
c = CLASS()
cc = CLASS()
 
print(c.x, c.y, c.z,c.w)


#from class_attr__instance_attr import CLASS
#import like above, make instances like c/cc
#are all defined CLASS.z only once

if __name__ == '__main__':
    print('23')
    if True :
        print(ret)
    else:
        print('done')