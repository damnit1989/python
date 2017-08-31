# -*- coding: utf-8 -*- 
# print('请输入你的名字:');
# name = input();
# print("你的名字是:",name);

# nameList = ['one','two','three']
# print(nameList);
# print(len(nameList));


' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
        print(args)
    elif len(args)==2:
        print('Hello, %s!' % args[1])
        print(args)
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()