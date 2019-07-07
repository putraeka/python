# Tutorial dari https://youtu.be/zjo9yFHoUl8

from selenium import webdriver
import csv
import time

max_page_num = 5
max_page_digit = 3

with open('results.csv', 'w') as f:
    f.write('Buyers,Price,\n')

browser = webdriver.Firefox()
# browser.get('http://econpy.pythonanywhere.com/ex/001.html')

for i in range(1, max_page_num + 1):
    page_num = (max_page_digit - len(str(i))) * "0" + str(i)
    url = f'http://econpy.pythonanywhere.com/ex/{page_num}.html'
    
    browser.get(url)
    
    # Extract lists of buyers and prices from xpath

    buyers = browser.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = browser.find_elements_by_xpath('//span[@class="item-price"]')

    # Print out all the buyers and prices in current page

    num_page_items = len(buyers)
    with open('results.csv', 'a') as f:
        for i in range(num_page_items):
            f.write(buyers[i].text + "," + prices[i].text + "\n")
    
    time.sleep(3)
# Clean browser once task is completed

browser.close()