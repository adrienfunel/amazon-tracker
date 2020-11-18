import requests
from bs4 import BeautifulSoup

from mail_app import email_service

URL = 'https://www.amazon.co.uk/Raspberry-Pi-ARM-Cortex-A72-Bluetooth-Micro-HDMI/dp/B07TC2BK1X/ref=sr_1_3?crid=3CHKCK8THJT9P&dchild=1&keywords=raspberry+pi+4&qid=1605655777&sprefix=raspberry%2Caps%2C158&sr=8-3'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}


def main():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_name = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    # price_float = float(price[1:])
    print(price)


    if product_name and price:
    	email_service(product_name.strip(), URL, price.encode('utf-8').strip())


if __name__ == "__main__":
	main()
