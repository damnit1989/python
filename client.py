# -*- coding: utf-8 -*- 
import socket
import json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
k = 0
dict = {'one':1,'two':2,'three':3,'four':4}
for data in [b'Michael', b'Tracy', b'Sarah',b'lmm']:
    # 发送数据:
    # s.send(data)
    s.send(json.dumps(dict))
    print(s.recv(1024))

s.send(b'exit')
s.close()