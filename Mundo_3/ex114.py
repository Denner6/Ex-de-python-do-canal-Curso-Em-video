import requests

def check_internet(url='http://pudim.com.br', timeout=5):
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False

if not check_internet():
    print('\033[31mO site pudim.com.br está inacessível no momento\033[m')
else:
    print('\033[32mO site pudim.com.br está acessível no momento\033[m')
