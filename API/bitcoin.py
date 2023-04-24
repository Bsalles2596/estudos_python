import requests

moeda = "BTC"
metodo = "ticker"

def get_bitcoin(moeda, metodo):
    url_api = f"https://www.mercadobitcoin.net/api/{moeda}/{metodo}/"
    req = requests.get(url_api)
    return req.json()
get = get_bitcoin(moeda, metodo)
print(get)
