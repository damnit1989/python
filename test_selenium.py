# -*- coding: utf-8 -*- 
# selenium示例

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


def search_from_baidu(word):
    try:

        driver = webdriver.Chrome()

        driver.get('https://www.baidu.com')
        elem = driver.find_element_by_name("wd")
        elem.clear()
        elem.send_keys(word)
        elem.send_keys(Keys.RETURN) 

        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print driver.page_source.encode('utf-8');
        driver.save_screenshot('screenshot.png')
        driver.get('https://www.baidu.com')
        # driver.forward()
        # driver.back()
        driver.save_screenshot('first.png')  
        assert 'dss' not in  driver.page_source 
        # driver.close()
    except AssertionError as e:
        pass
        # print dir(e)
        # print type(e)
        # print e.msg
        # print 'assert 1==2'
    except Exception as e:
        print e
        pass
        # print dir(e)
        # # print e.__init__
        # print e.message

def test_django():
    try:
        
        # driver = webdriver.Firefox()
        driver = webdriver.Chrome()

        driver.get('http://192.168.17.134:8000/accounts/login/')
        driver.find_element_by_xpath("//div/input[@name='username']").send_keys('lmm')
        # driver.find_element_by_name("username").send_keys('lmm')
        driver.find_element_by_xpath("//div/input[@name='password']").send_keys('lmm-3971655')
        driver.find_element_by_xpath("//input[@type='submit']").click()
        # elem.send_keys(Keys.RETURN) 


        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print driver.page_source.encode('utf-8')
        
        driver.save_screenshot('screenshot.png')
        driver.get('http://192.168.17.134:8000/online/login/')
        
        time.sleep(3)
        # 隐式等待是等待特定的时间，显式等待是指定某一条件直到这个条件成立时继续执行
        
        # 隐式等待
        driver.implicitly_wait(10) # seconds
        
        #显式等待
        element = WebDriverWait(driver,3).until(
            EC.presence_of_element_located((By.ID,'id_username'))
        )
        
        driver.save_screenshot('first.png') 
        driver.find_element_by_xpath("//input[@name='username']").send_keys('lmm')
        driver.find_element_by_xpath("//input[@name='password']").send_keys('123456')
        driver.find_element_by_xpath("//input[@type='submit']").click()
        
        driver.save_screenshot('two.png')         
        driver.find_element_by_link_text("列表").click()
        # print driver.page_source().encode('utf-8')
        # driver.forward()
        # driver.back()
        driver.save_screenshot('three.png')  
        # assert 'dss' not in  driver.page_source 
        # driver.close()
    except AssertionError as e:
        pass
        # print dir(e)
        # print type(e)
        # print e.msg
        # print 'assert 1==2'
    except Exception as e:
        print e
        pass
        # print dir(e)
        # # print e.__init__
        # print e.message    
if __name__ == '__main__':
    # test_django()
    word = str(input('请输入你要查询的字符:'))

    search_from_baidu(word)