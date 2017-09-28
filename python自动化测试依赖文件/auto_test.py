# -*- coding: utf8 -*-
 
import sys
import re
import time
from splinter.browser import Browser
# from splinter import Browser
 
 
# from selenium import webdriver

# chromedriver = "D:\Program Files\Mozilla Firefox\firefox.exe"

# from selenium import webdriver

# browser = webdriver.Firefox()
# driver = webdriver.Firefox()

# driver.get('http://stackoverflow.com')

# driver.quit()
# from selenium import webdriver

# driver = webdriver.Chrome()
# driver = webdriver.Chrome('C:\Python27\chromedriver') 
#####################################################
# global instance
CLOASE_AFTER_TEST = False
GBK = "gbk"
UTF8 = "utf8"
 
#####################################################
# encoding for console
reload(sys)
sys.setdefaultencoding(UTF8)
 
#####################################################
# small method
encoding = lambda x:x.encode('gbk')
 
#####################################################
def output(x):
    """
        encode and print
    """
    print encoding(x)
 
def resultMsg(x):
    """
        judge result and print, x : True or False
    """
    if x == True:
        print 'pass'
    else:
        print '[X]not pass'
    print '--------------------------'
 
def checkresult(x):
    """
        check result message, x : the error message u want
    """
    resultMsg(browser.is_text_present(x))
 
def testLogin(desc, username, password, result):
    """
        fill login form message and submit, check result message and print
    """
    output(desc)
    browser.fill('user_name',username.decode(UTF8))
    browser.fill('user_password',password.decode(UTF8))
    # browser.find_by_value('登录').first.click()
    browser.find_by_text('登录').first.click()    
    checkresult(result)
 
def testAddUser(desc,userName,name,age,country,school,pwd,result):
    output(desc)
    browser.fill('user',userName.decode(UTF8))
    browser.fill('name',name.decode(UTF8))
    # browser.fill('gender',sex)
    browser.fill('age',age)
    browser.fill('country',country.decode(UTF8))
    browser.fill('academy',school.decode(UTF8))
    browser.fill('password',pwd.decode(UTF8))
    browser.find_by_id('save_written_btn').first.click()
    checkresult(result)    
 
# chrome driver : http://code.google.com/p/selenium/wiki/ChromeDriver
# already support firefox
# browser = Browser()
browser = Browser('chrome')

 
try:
    
    #测试管理端登录   
    __loginUrl = 'http://192.168.201.100:8282/nrtadmin/login'
    browser.visit(__loginUrl)
    output("测试页面:"+browser.title)   

    testLogin('测试未输入用户名','','qq1122','请填写用户名')
    testLogin('测试未输入密码','admin','','请填写密码')
    testLogin('测试帐户不存在','qq','123456','用户名或者密码错误！')
    testLogin('测试成功登录','admin','qq1122','继续登录前操作')
 
 
    #测试添加用户
    time.sleep(2)       
    output("接下来测试添加用户")
    # __userUrl = "http://192.168.201.100:8282/nrtadmin/users/ajax-tpl?act=users"
    # browser.visit(__userUrl)
    time.sleep(3)   
    browser.find_by_id('add_user').first.click()
    time.sleep(3)
    testAddUser('测试完整填写','xxxxx','lmm',27,'中国','西普','123456','操作成功')

 
except Exception,x:
    print x
 
if CLOASE_AFTER_TEST:
    browser.quit()