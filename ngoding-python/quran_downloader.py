import requests
from url_generator import generator
import progressbar

kumpulanUrl = generator() # url qur'an per juz

for i in progressbar.progressbar(range(len(kumpulanUrl))):

    r = requests.get(kumpulanUrl[i])

    filename = 'quran/'+kumpulanUrl[i].split('/')[-1]

    with open(filename, 'wb') as f:
        f.write(r.content)