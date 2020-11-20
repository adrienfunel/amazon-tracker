import requests
from bs4 import BeautifulSoup
import re


def get_soup(url, headers):
    """Extract soup from HTML source code."""
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup


def extract_pricing_data(soup):
    """Scrap pricing data from bs4 soup."""
    product_name = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    price_value = re.findall(r'\d+\.\d+', price)[0]
    price_currency = soup.find('div', {'id': 'cerberus-data-metrics'})['data-asin-currency-code']

    return product_name, price_value, price_currency
