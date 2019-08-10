import requests
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-l','--link',required=True,help='link file')
args = vars(ap.parse_args())

r = requests.get(args['link'])

filename = args['link'].split('/')[-1]

# url = 'https://forum.manjaro.org/uploads/default/original/3X/6/7/67498ebb144f6aca69e64cd53b1ed6234a935427.png'
# r = requests.get(url)

with open(filename, 'wb') as f:
    f.write(r.content)