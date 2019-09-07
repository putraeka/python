import requests
from bs4 import BeautifulSoup

# Reference:
# website login using requests library : https://www.youtube.com/watch?v=fmf_y8zpOgA

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0'}

payload = {
    'name':	"username",
    "pass":	"pass",
    'form_id':	"new_login_form",
    'op': "Login"
}

with requests.Session() as s:
    url = 'https://www.codechef.com/'
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    payload['form_build_id'] = soup.find('input', attrs={'name': 'form_build_id'})['value']

    r = s.post(url, data=payload, headers=headers)
    
    print(r.content)