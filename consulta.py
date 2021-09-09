import requests

apikey = "23DBFF71-249C-46BB-BB56-9EBDFA5399F6"
url = "https://rest.coinapi.io/v1/exchangerate/BTC/EUR"

cabecera = {"X-CoinAPI-Key": apikey}
respuesta = requests.get(url, headers=cabecera)

print(respuesta.status_code)
midiccionario = respuesta.json()
print(midiccionario['rate'])

print(respuesta.json()["rate"])