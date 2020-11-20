import requests
from bs4 import BeautifulSoup
import re

from constants import URL, headers
from mail_app import email_service


def main():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_name = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    price_currency = soup.find('div', {'id': 'cerberus-data-metrics'})['data-asin-currency-code']
    price_value = re.findall(r'\d+\.\d+', price)[0]

    if product_name and price and float(price_value) < 60:
        email_service(product_name.strip(), URL, price_value, price_currency)


if __name__ == '__main__':
    main()
