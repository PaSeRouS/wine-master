import argparse
import collections
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", default='products.xlsx')
    args = parser.parse_args()

    current_year = datetime.now().year
    winery_age = current_year - 1920

    products = pandas.read_excel(args.filename, sheet_name='Лист1', keep_default_na=False).to_dict(orient='records')

    collection_of_products = collections.defaultdict(list)

    for product in products:
        product['Цена'] = int(product['Цена'])
        collection_of_products[product['Категория']].append(product)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        winery_age=winery_age,
        collection_of_products=collection_of_products,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
