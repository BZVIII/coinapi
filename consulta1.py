import requests

apikey = "23DBFF71-249C-46BB-BB56-9EBDFA5399F6"
url = "https://rest.coinapi.io/v1/exchangerate/{}/{}"

cabecera = {"X-CoinAPI-Key": apikey}

seguir = 's'
while seguir == 's':
    de = input("Moneda de origen: ")
    a = input("Moneda de destino: ")
    respuesta = requests.get(url.format(de, a), headers=cabecera)

    if respuesta.status_code == 200:
        print(respuesta.json()["rate"])
    else:
        print(respuesta.status_code)
        print(respuesta.json())

    seguir = input("Quieres más (S/N): ").lower()
