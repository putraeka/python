# Tutorial dari https://youtu.be/GJjMjB3rkJM

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://www.seleniumhq.org/')

elem = browser.find_element_by_link_text('Download')

elem.text
elem.get_attribute('href')
elem.click()

searchBar = browser.find_element_by_id('q')
searchBar.send_keys('download')
searchBar.send_keys(Keys.ENTER)