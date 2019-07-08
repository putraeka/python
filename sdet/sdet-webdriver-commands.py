# Tutorial dari https://www.youtube.com/watch?v=NYA7AVdD4hA

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path='/home/aei/Documents/codes/python/driver/chromedriver')
url = 'http://demo.automationtesting.in/Windows.html'

browser.get(url)

print(browser.title) # Get title of the page
print(browser.current_url) # return current url of the page

browser.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

time.sleep(5)

# fungsinya sama seperti Ctrl + w (close one with window at a time)
browser.close()

time.sleep(5)

# jika ingin close semua windows seperti Mod4 + q di i3 atau tombol x gunakan
browser.quit()