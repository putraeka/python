import requests

API_KEY = '4924dfdfb9c0499183922ebf2975da76'

def city(aidi, province, key=API_KEY):
    url = 'https://api.rajaongkir.com/starter/city'

    query_params = {
        'id': aidi,
        'province': province,
        'key': key
    }
    
    response = requests.get(url, params=query_params)

    return response.json()