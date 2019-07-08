# Tutorial dari https://youtu.be/9_xCp1qGek4

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path='/home/aei/Documents/codes/python/driver/chromedriver')
url = 'http://newtours.demoaut.com/'
url2 = 'http://putraeka.org'

browser.get(url)
print(browser.title)
time.sleep(15)
browser.get(url2)
print(browser.title)
time.sleep(15)
browser.back()
print(browser.title)
time.sleep(15)
browser.forward()
print(browser.title)
time.sleep(15)

browser.quit()