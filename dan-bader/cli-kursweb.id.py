import requests
import click


def bank(nama_bank):
    url = 'https://kurs.web.id/api/v1/'
    
    response = requests.get(url)

    return response.json()['jual']