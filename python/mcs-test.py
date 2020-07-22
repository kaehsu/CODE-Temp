# -*- coding: utf-8 -*-
#
# PRE: go to http://chromedriver.chromium.org/downloads to download chromedriver.exe
#

import sys
import time

sys.path.append('/d/temp/test/')                                # my path to chromedriver.exe, modify this for your environment

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
#option.add_argument('headless')                                # don't add this if we want to watch browser opened (headless is specially for crawler to read web page)
#option.add_argument('disable-gpu')                             # omit some Lost UI error, but seems not necessary here... I just marked it

driver = webdriver.Chrome(chrome_options=option)

#driver = webdriver.Chrome()
#driver = webdriver.PhantomJS()                                 # old age method

driver.get('http://portal.xgds.net/MCSCss/BPi-A/mcsclab/')
print('open browser')
print(driver.title)

# wait for password: prompt
try:
    wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'password:')]")))
    print('got password prompt')
    ele_id = driver.switch_to.active_element

    if ele_id:
        print(ele_id)
        ele_id.send_keys('PASSWORD of ...')
        ele_id.send_keys(Keys.RETURN)
        time.sleep(3)    # just for debugging
        ####wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@id='reconnect']/input[contains(text(),'System')]")))
        ele_id = driver.switch_to.active_element
        ele_id.send_keys('e')
        time.sleep(3)    # just for human's eyes
        ele_id.send_keys('e')
        time.sleep(3)    # just for human's eyes
        ele_id.send_keys(Keys.RETURN)
        time.sleep(3)    # just for human's eyes
    else:
        print('ele_id not found')

    # by DOM id (if we had it already)
    ####ele_id = driver.find_element_by_id('lst-ib')     # this is https://www.google.com.tw/ 's search text box
    ####ele_id.send_keys('test')
    ####ele_id.submit()
    ####print('close')
finally:
    driver.quit()
    print('test done')

