"""
This file needs for use the bot logic.
simple function helps us search and parsing the information.
Version: 0.1
Developer: Rudich ILya
"""
import time
import requests
from bs4 import BeautifulSoup

XRP_DOLLAR = 'https://coinmarketcap.com/currencies/xrp/'
BNB_DOLLAR = 'https://www.coingecko.com/en/coins/binance-coin'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/89.0.4389.128 Safari/537.36'}


def xrp_value():
    full_page = requests.get(XRP_DOLLAR, headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.find("div", {"class": "priceValue___11gHJ"})
    convert = str(convert)
    convert = convert[33:37]
    ripple = convert
    return ripple


def bnb_value():
    full_page = requests.get(BNB_DOLLAR, headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.find("span", {"data-target": "price.price"})
    convert = str(convert)
    convert = convert[128:133]
    bnb = convert
    return bnb
