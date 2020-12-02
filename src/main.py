from constants import URL, headers
from mail_app import email_service
from apps import get_soup, extract_pricing_data
from time import perf_counter


def main():
    """This is the main endpoint."""
    soup = get_soup(URL, headers)
    product_name, price_value, price_currency = extract_pricing_data(soup)

    if product_name and price_value and float(price_value) < 60:
        email_service(product_name.strip(), URL, price_value, price_currency)


if __name__ == '__main__':
    start = perf_counter()

    main()

    end = perf_counter()
    elapsed = end - start
    print(f"Elapsed time in seconds {elapsed:0.2f}")
