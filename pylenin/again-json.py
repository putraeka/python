import json
import requests

# data = json.load(open('MGEX_IH1.json'))

# print(type(data))

url = 'https://www.quandl.com/api/v3/datasets/CHRIS/MGEX_IH1.json?api_key=_ieUYv3uU4s7jh_eoo99'

request= requests.get(url)
request_text= request.text
data = json.loads(request_text)
# data_serialized_string = json.dumps(data)
json.dump(data, open('quandl-mgex.json', 'w'), indent=2)


# print(type(data))
# print(type(data_serialized))