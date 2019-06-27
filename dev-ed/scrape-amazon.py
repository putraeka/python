import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8'
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'lxml')

# title = soup.find(id="productTitle").get_text()
#price = soup.find('div', attrs={id="olp-sl-new-used", "class_":"a-color-price"}).get_text()
#pricegroup = soup.find(id="olp-sl-new-used")
#price = soup.find_all(id="productTitle", {'class': 'a-color-price'}) 
#converted_price = price[0:8]

#print(title.strip())
#print(price)

# price = soup.find_all('span')
# price_tag = price.find_all('olp-sl-new-used')
# for tag in price_tag:
#     print(tag)
# for tag in price:
#     if "olp-sl-new-used" in price.attrs:
#         print(tag)

price = soup.find_all(class_='a-color-price')[2].string
price_stripped = price[0:5]
print(price_stripped)