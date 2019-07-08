# Tutorial dari https://youtu.be/1spPl1GbVUU

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(executable_path='/home/aei/Documents/codes/python/driver/chromedriver')
url = 'http://newtours.demoaut.com/'
browser.get(url)
elm = browser.find_element_by_name('userName')
passwd = browser.find_element_by_name('password')
login_btn = browser.find_element_by_name('login')
roundtrip_radio = browser.find_element_by_css_selector("input[value=roundtrip]")
roundtrip_oneway = browser.find_element_by_css_selector("input[value=oneway]")

print(elm.is_displayed()) # apakah elementnya displayed or not? Boolean
print(elm.is_enabled()) # apakah elementnya enabler or not? Boolean

elm.send_keys('mercury')
passwd.send_keys('mercury')
time.sleep(3)
login_btn.click()

print(roundtrip_radio.is_selected())
print(roundtrip_oneway.is_selected())

browser.close()