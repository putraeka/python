# Tutorial dari https://youtu.be/XQgXKtPSzUI?list=WL

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# Opening the connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# HTML parsing
page_soup = soup(page_html, "html.parser")

# Grab each graphic card images
containers = page_soup.find_all("div",{"class":"item-container"})

filename = "newegg-graphics-card.csv"
f = open(filename, 'w')
headers = "brand, product_name, shipping, \n"
f.write(headers)

for container in containers:
    try:
        brand = container.find("a",{"class":"item-brand"}).img["title"]
        product_name = container.find("a", {"class":"item-title"}).text
        shipping = container.find("li", {"class":"price-ship"}).text.strip()
    except Exception as e:
        brand = "None"
    
    print("brand :" + brand)
    print("product_name :" + product_name)
    print("shipping : " + shipping)

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()