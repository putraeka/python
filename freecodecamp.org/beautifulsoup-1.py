import requests
from bs4 import BeautifulSoup

results = requests.get('https://www.google.com')
# Check status code dari website (200 = server ok)
# print(results.status_code)
# Check header
# print(results.headers)

# Menyimpan hasil request ke variable src
src = results.content

# Store object to beautifulsoup
soup = BeautifulSoup(src, 'lxml')

# Cari tags 'a'
links = soup.find_all('a')

# Cari anchor text about
for link in links:
    if "Serba-serbi" in link.text:
        print(link)
        print(link.attrs['href'])