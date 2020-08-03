import requests
URL = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5201"

def ziskej_odpoved():
    return requests.get(URL)