"""A Python3 based NF reader."""


import re
import requests
import argparse
from bs4 import BeautifulSoup


def to_us_number(number):
    """Convert string number representation to float.

    Keyword argument:
        number -- string with number
    """
    number = number.replace('.', '')
    number = number.replace(',', '.')

    return float(number)


def read_nf(url):
    """Read a NF from an URL and return a list of items."""
    # List of items
    cart = list()

    # Get request from URL
    html = requests.get(url)

    # Parse response
    text = BeautifulSoup(html.text, 'html.parser')

    # Items from table
    items = text.find_all('table', attrs={'class': 'NFCCabecalho'})
    items = items[3].find_all('tr')

    # Filter data
    del items[0]

    # For each item in table...
    for i in items:
        # Get details
        details = i.find_all('td')

        # Add item to cart
        cart.append({
            'name': re.sub('(\s+)', ' ', details[1].get_text()),
            'quantity': to_us_number(details[2].get_text()),
            'price': to_us_number(details[4].get_text())
        })

    return cart


def main(args):
    """Execute in shell."""
    if not (args.file is None):
        # List of items
        items = list()

        # Open file
        urls = open(args.file, 'r')

        # For each url in file...
        for url in urls:
            items += read_nf(url)

        # Close file
        urls.close()
    else:
        # Only one url
        items = read_nf(args.url)

    # Print results
    form = "{:<60}{:>5}{:>8}"

    print(form.format('Name', 'Qty', 'Price'))

    # For each item...
    for item in items:
        print(form.format(item['name'], item['quantity'], item['price']))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file",
                        dest="file",
                        default=None,
                        help="Input filepath.")

    parser.add_argument("-u", "--url",
                        dest="url",
                        help="NF url.")

    args = parser.parse_args()
    main(args)
