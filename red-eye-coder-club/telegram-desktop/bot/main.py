# library
import requests
import json
import re
from flask import Flask
from flask import request
from flask import Response
from flask_sslify import SSLify

# functions
from tokens import cmc_token
from tokens import telegram_token

# telegram Api
# https://api.telegram.org/bot948146242:AAHXZET2uYfQ7321FHAcqvQQbbTfY7xsK70/getUpdates
# https://api.telegram.org/bot948146242:AAHXZET2uYfQ7321FHAcqvQQbbTfY7xsK70/sendMessage?chat_id=174709034&text=hello%20user
# https://api.telegram.org/bot948146242:AAHXZET2uYfQ7321FHAcqvQQbbTfY7xsK70/setWebhook?url=https://quarum.serveo.net/
# Codes

app = Flask(__name__)
sslify = SSLify(app)

def write_json(data, filename='response.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_cmc_data(crypto):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {
        'symbol': crypto,
        'convert': 'USD'
    }

    header = {
        'X-CMC_PRO_API_KEY': cmc_token
    }
    
    r = requests.get(url, headers=header, params=params).json()
    price = r['data'][crypto]['quote']['USD']['price']
    # write_json(r)
    
    return price
    
def parse_message(message):
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    
    pattern = r'/[A-z]{2,4}'
    ticker = re.findall(pattern, txt)

    if ticker:
        symbol = ticker[0][1:].upper()
    else:
        symbol = ''
    
    return chat_id, symbol

def send_message(chat_id, text='bla-bla-bla'):
    url = f"https://api.telegram.org/{telegram_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    
    r = requests.post(url, json=payload)
    return r
    
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        chat_id, symbol = parse_message(msg)
        
        if not symbol:
            send_message(chat_id, 'wrong data')
            return Response('Ok', status=200)
        
        price = get_cmc_data(symbol)
        send_message(chat_id, price)
        write_json(msg, 'telegram_response.json')
        
        return Response('Ok', status=200)
    else:
        return '<h1>CoinMarketCap Bot</h2>'

def main():
    print(get_cmc_data('BTC'))


if __name__ == "__main__":
    # main()
    app.run(debug=True)