# -*- coding: utf-8 -*- 
# selenium示例

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time 
try:

    driver = webdriver.Firefox()

    driver.get('https://www.baidu.com')
    elem = driver.find_element_by_name("wd")
    elem.clear()
    elem.send_keys('python')
    elem.send_keys(Keys.RETURN) 

    time.sleep(5)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print driver.page_source;
    driver.save_screenshot('screenshot.png')
    assert '很抱歉' not in  driver.page_source 
    driver.close()
except AssertionError as e:
    print dir(e)
    print type(e)
    print 'assert 1==2'
except Exception,e:
    print dir(e)
    # print e.__init__
    print e.message

