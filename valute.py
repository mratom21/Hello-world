import json
from multiprocessing import Value
import requests
from pprint import pprint
from bs4 import BeautifulSoup
import requests 
import lxml

money = 0
USD = 0
EUR = 0
ETH = 0
BTC = 0
DOGE = 0

def get_btc():
    url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=ETH,BTC,DOGE&tsyms=USD&api_key=INSERT-cf0ef631d331819030a8ee6cfed755341ee2ee5f5310db8ca3fbe634db7620a9'
    req = requests.get(url)
    data_btc = req.json()
    return data_btc


def get_valute():
    data_btc = get_btc()

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
    }
    
    req = requests.get('https://ru.investing.com/currencies/usd-rub', headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    # with open ('index.html', 'wt', encoding='utf-8') as file:
    #     file.write(req.text)
    USD = float((str(soup.find('span', class_='text-2xl').text)).replace(',', '.'))
    RUB_USD = f'USD/RUB - {USD} р'

    req = requests.get('https://ru.investing.com/currencies/eur-rub', headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    EUR = float((str(soup.find('span', class_='text-2xl').text)).replace(',', '.'))
    RUB_EUR = f'EUR/RUB - {EUR} р'

    req = requests.get('https://ru.investing.com/currencies/uah-rub', headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    UAH = float((str(soup.find('span', class_='text-2xl').text)).replace(',', '.'))
    RUB_UAH = f'UAH/RUB - {UAH} р'

    ETH = (data_btc['ETH']['USD'])
    ETH_USD = f'ETH/USD - $ {ETH}'

    BTC = (data_btc['BTC']['USD'])
    BTC_USD = f'BTC/USD - $ {BTC}'
    
    DOGE = (data_btc['DOGE']['USD'])

    Value = (f'\n=============\n🇺🇸 USD - {RUB_USD}\n🇪🇺 EUR - {RUB_EUR}\n🇺🇦 UAH - {RUB_UAH}\n=============\nETH/USD - {ETH_USD} eth\nBTC/USD - {BTC_USD} btc')
    # print(Value)
    return Value


def check_currensy(money):   
    currency = ('р', 'руб', 'долларов', 'доллар', 'евро', 'гривен', 'дол', 'рублей', 'дл', 
    'уе', 'usd', 'еу', 'eur', 'рубль', 'rub', 'гривна', 'гр', 'uah', 'btc', 'биткоин', 
    'биток', 'биткоинов', 'eth', 'эфир', 'эфириум', 'кефир', '')
    for cyr in currency:
        try:
            r = money.strip(cyr)
            result = float(r)
            # print(cyr)
            return(cyr)
        except:
            pass

def get_btc():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
    }
    url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=ETH,BTC,DOGE&tsyms=USD&api_key=INSERT-cf0ef631d331819030a8ee6cfed755341ee2ee5f5310db8ca3fbe634db7620a9'
    req = requests.get(url)
    data_btc = req.json()
    return data_btc

def get_usd():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
    }
    req = requests.get('https://ru.investing.com/currencies/usd-rub', headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    USD = float((str(soup.find('span', class_='text-2xl').text)).replace(',', '.'))
    return USD

def get_eur():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
    }
    req = requests.get('https://ru.investing.com/currencies/eur-rub', headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    EUR = float((str(soup.find('span', class_='text-2xl').text)).replace(',', '.'))
    return EUR

def get_uah():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
    }
    req = requests.get('https://ru.investing.com/currencies/uah-rub', headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    UAH = float((str(soup.find('span', class_='text-2xl').text)).replace(',', '.'))
    return UAH

def calc_valute(money):
    usd_lis=['долларов', 'доллар', 'дол', 'дл', 'уе', 'usd']
    eur_lis=['евро', 'еу', 'eur']
    rub_lis=['р', 'руб', 'рублей', 'рубль', 'rub']
    uah_lis=['гривен', 'гривна', 'гр', 'uah']
    btc_lis=['btc', 'биткоин', 'биток', 'биткоинов']
    eth_lis=['eth', 'эфир', 'эфириум', 'кефир']
    UAH = get_uah()
    USD = get_usd()
    EUR = get_eur()
    data_btc = get_btc()
    ETH = (data_btc['ETH']['USD'])
    BTC = (data_btc['BTC']['USD'])

    cur = str(check_currensy(money))
    # print(cur)

    if cur in rub_lis:
        money = float((str(money)).strip(cur))
        calc_usd = money/USD
        calc_usd = float('{:.2f}'.format(calc_usd))
        calc_eur = money/EUR
        calc_eur = float('{:.2f}'.format(calc_eur))
        calc_uah = money/UAH
        calc_uah = float('{:.2f}'.format(calc_uah))
        calc_eth = calc_usd/ETH
        calc_eth = float('{:.6f}'.format(calc_eth))
        calc_btc = calc_usd/BTC
        calc_btc = float('{:.8f}'.format(calc_btc))
        calc = (f'🇷🇺 {money} {cur}\n=============\n🇺🇸 USD - {calc_usd}\n🇪🇺 EUR - {calc_eur}\n🇺🇦 UAH - {calc_uah}\n=============\nETH/USD - {calc_eth} eth\nBTC/USD - {calc_btc} btc')
        # print(calc)
    elif cur in usd_lis:
        money = float((str(money)).strip(cur))
        calc_rub = money*USD
        calc_rub = float('{:.2f}'.format(calc_rub))
        calc_eur = (money*USD)/EUR
        calc_eur = float('{:.2f}'.format(calc_eur))
        calc_uah = (money/UAH)*USD
        calc_uah = float('{:.2f}'.format(calc_uah))
        calc_eth = money/ETH
        calc_eth = float('{:.6f}'.format(calc_eth))
        calc_btc = money/BTC
        calc_btc = float('{:.8f}'.format(calc_btc))
        calc = (f'🇺🇸 {money} {cur}\n=============\n🇷🇺 RUB - {calc_rub}\n🇪🇺 EUR - {calc_eur}\n🇺🇦 UAH - {calc_uah}\n=============\nETH/USD - {calc_eth} eth\nBTC/USD - {calc_btc} btc')
        # print(calc)
    elif cur in eur_lis:
        money = float((str(money)).strip(cur))
        calc_rub = money*EUR
        calc_rub = float('{:.2f}'.format(calc_rub))
        calc_usd = (money*EUR)/USD
        calc_usd = float('{:.2f}'.format(calc_usd))
        calc_uah = (money/UAH)*EUR
        calc_uah = float('{:.2f}'.format(calc_uah))
        calc_eth = ((money*EUR)/USD)/ETH
        calc_eth = float('{:.6f}'.format(calc_eth))
        calc_btc = ((money*EUR)/USD)/BTC
        calc_btc = float('{:.8f}'.format(calc_btc))
        calc = (f'🇪🇺 {money} {cur}\n=============\n🇷🇺 RUB - {calc_rub}\n🇺🇸 USD - {calc_usd}\n🇺🇦 UAH - {calc_uah}\n=============\nETH/USD - {calc_eth} eth\nBTC/USD - {calc_btc} btc')
        # print(calc)
    elif cur in uah_lis:
        money = float((str(money)).strip(cur))
        calc_rub = money*UAH
        calc_rub = float('{:.2f}'.format(calc_rub))
        calc_usd = (money*UAH)/USD
        calc_usd = float('{:.2f}'.format(calc_usd))
        calc_eur = (money*UAH)/EUR
        calc_eur = float('{:.2f}'.format(calc_eur))
        calc_eth = ((money*UAH)/USD)/ETH
        calc_eth = float('{:.6f}'.format(calc_eth))
        calc_btc = ((money*UAH)/USD)/BTC
        calc_btc = float('{:.8f}'.format(calc_btc))
        if money == 40:
            calc = (f'🇺🇦 {money} {cur}\n=============\n🇷🇺 RUB - {calc_rub}\n🇺🇸 USD - {calc_usd}\n🇪🇺 EUR - {calc_eur}\n=============\nETH/USD - {calc_eth} eth\nBTC/USD - {calc_btc} btc\n\nШтаны за 40 гривен?')
            # return calc
            # print(calc)
        else:
            calc = (f'🇺🇦 {money} {cur}\n=============\n🇷🇺 RUB - {calc_rub}\n🇺🇸 USD - {calc_usd}\n🇪🇺 EUR - {calc_eur}\n=============\nETH/USD - {calc_eth} eth\nBTC/USD - {calc_btc} btc')
    elif cur in btc_lis:
        money = float((str(money)).strip(cur))
        calc_rub = money*BTC*USD
        calc_rub = float('{:.2f}'.format(calc_rub))
        calc_usd = money*BTC
        calc_usd = float('{:.2f}'.format(calc_usd))
        calc_eur = (money*BTC*USD)/EUR
        calc_eur = float('{:.2f}'.format(calc_eur))
        calc_uah = (money*BTC*USD)*UAH
        calc_uah = float('{:.2f}'.format(calc_uah))
        calc_eth = (money*BTC)/ETH
        calc_eth = float('{:.6f}'.format(calc_eth))
        calc = (f'{money} {cur}\n=============\n🇷🇺 RUB - {calc_rub}\n🇺🇦 UAH - {calc_uah}\n🇺🇸 USD - {calc_usd}\n🇪🇺 EUR - {calc_eur}\n=============\nETH/USD - {calc_eth} eth')
    elif cur in eth_lis:
        money = float((str(money)).strip(cur))
        calc_rub = money*ETH*USD
        calc_rub = float('{:.2f}'.format(calc_rub))
        calc_usd = money*ETH
        calc_usd = float('{:.2f}'.format(calc_usd))
        calc_eur = (money*ETH*USD)/EUR
        calc_eur = float('{:.2f}'.format(calc_eur))
        calc_uah = (money*ETH*USD)/UAH
        calc_uah = float('{:.2f}'.format(calc_uah))
        calc_btc = (money*ETH)/BTC
        calc_btc = float('{:.6f}'.format(calc_btc))
        calc = (f'{money} {cur}\n=============\n🇷🇺 RUB - {calc_rub}\n🇺🇦 UAH - {calc_uah}\n🇺🇸 USD - {calc_usd}\n🇪🇺 EUR - {calc_eur}\n=============\nBTC/USD - {calc_btc} btc')
    elif cur == '':
        calc = 'Я не понял, что ты написал. Я надеюсь ты не забыл указать валюту или само число?'
    return calc
    # print(calc)
        


def main():
    get_valute()

if __name__ == '__main__':
    main()