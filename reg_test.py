#!/usr/bin/python2
# -*- coding: utf-8 -*-
# 正则表达式


import re

str = " i love you very much"
patten = '^.\w+$'
L = re.findall(patten,str)
print L
print type(L)
for item in L:
    print item
    
    
s = 'This and That'
data = re.findall(r'(th\w+) and (th\w+)',s,re.I)
print data


# # 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
# pattern = re.compile(r'hello')
 
# # 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
# result1 = re.match(pattern,'hello')
# result2 = re.match(pattern,'helloo CQC!')
# result3 = re.match(pattern,'helo CQC!')
# result4 = re.match(pattern,'hello CQC!')
 
# #如果1匹配成功
# if result1:
    # # 使用Match获得分组信息
    # print result1.group()
# else:
    # print '1匹配失败！'
 
 
# #如果2匹配成功
# if result2:
    # # 使用Match获得分组信息
    # print result2.group()
# else:
    # print '2匹配失败！'
 
 
# #如果3匹配成功
# if result3:
    # # 使用Match获得分组信息
    # print result3.group()
# else:
    # print '3匹配失败！'
 
# #如果4匹配成功
# if result4:
    # # 使用Match获得分组信息
    # print result4.group()
# else:
    # print '4匹配失败！'
    
    
    
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
 
print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')
 
### output ###
# m.string: hello world!
# m.re: 
# m.pos: 0
# m.endpos: 12
# m.lastindex: 3
# m.lastgroup: sign
# m.group(1,2): ('hello', 'world')
# m.groups(): ('hello', 'world', '!')
# m.groupdict(): {'sign': '!'}
# m.start(2): 6
# m.end(2): 11
# m.span(2): (6, 11)
# m.expand(r'\2 \1\3'): world hello!


if __name__ == '__main__':
    import json
    
    a = {
        "444625f6fd3311e5800000163e514738": {
            "email": "",
            "language": "zh_CN",
            "level": "ERROR",
            "phone": "",
            "types": ["email", "sms"]
        },
        "5e4fb6ec523d11e6800000163e514738": {
            "email": "123@qq.com",
            "language": "zh_CN",
            "level": "ERROR",
            "phone": "12341231234",
            "types": ["email", "sms"]
        }
    }
    for k,v in a.items():
        print k,'的电话号码:',v['phone']
        
    # print list
    