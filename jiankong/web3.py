# -*- coding: utf-8 -*- 
from socket import *
import time
import json
import paramiko
import hashlib
import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('config.cfg','rb'))

HOST = config.get("global","HOST")          #主机名
PORT =  config.get("global","PORT")             #端口号 与服务器一致
BUFSIZE = 1024              #缓冲区大小1K
ADDR = (HOST,int(PORT))
TIME = 6*int(config.get("global","TIME"))                 #60秒乘分钟，因为检测的时间间隔还没确定，确定之后只需要将1改掉
ISOTIMEFORMAT='%Y-%m-%d %X'
SCORE = int(config.get("global","SCOR"))                  #每道题目的分数，定义为常量，比较好修改
NUM = 3                     #此处定义没到题目的编号

TEAMNAME = config.get("global","TEAMNAME") 		#此处定义队伍的名字
GroupId = config.get("global","GroupId")               #队伍组id
AreaId   = 5				#区域id
ServerID = "8"              #服务器ID

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)    #连接服务器
data = {"timestamp":"","score":0,"num":0,"type":"1","repair":False,"reason":"","signature":"","group_id":GroupId,"device_id":ServerID,"area_id":AreaId} #发送给服务器的字典

def checkkey():
    signature = hashlib.sha1(str(int(time.time()))+ServerID+'5acf83856c97a3c031212fd37b7aa1ca').hexdigest()
    return signature

def checkPort():
    #以下是检测80端口是否被关闭
    sk = socket(AF_INET, SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect(('192.168.200.84',22))
        sk.close()
    except Exception:
        sk.close()
        return False
    return True

def checkVul():
    #以下是检测程序的文件包含漏洞是否修补
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='192.168.200.84',username='root',password='123456',timeout=5)
        ssh.close()
        data['timestamp']=int(time.time())
        data['score']=0
        data['num'] = NUM
        data['reason'] = '192.168.5.11-web3 password not modified'
        data['type']  = 1  #扣分类型 1加分2减分
        data['signature'] = checkkey()
        data['group_id']  = GroupId
        data['device_id'] = ServerID
        data['area_id']   = AreaId
    except Exception:
        data['timestamp']=int(time.time())
        if data['repair'] == False:     #第一次加分多一些
            data['score']=SCORE
        else:                           #之后每次检测都按照本题分数的百分比加分
            data['score']=SCORE*0.2
        data['num'] = NUM
        data['repair'] = True
        data['reason'] = '192.168.5.11-web3 password has been modified'
        data['type']  = 1  #扣分类型 1加分2减分
        data['signature'] = checkkey()
        data['group_id']  = GroupId
        data['device_id'] = ServerID
        data['area_id']   = AreaId

    json_str=json.dumps(data)           #编码json
    tcpCliSock.send(json_str)           #发送数据
checkVul()
# while True:                 #无限循环等待连接到来
    # time.sleep(TIME)
    # try:
        # if checkPort():
            # checkVul()
        # else:
            # continue

        # if not data:
            # break
    # except Exception,e:
        # print 'Error: ',e

tcpCliSock.close()          #关闭客户端
