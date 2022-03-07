import collections
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pprint import pprint

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


if __name__ == '__main__':
    now = datetime.now()
    years_from_foundation = now.year - 1920

    excel_data = pandas.read_excel('wine.xlsx', sheet_name='Лист1', keep_default_na=False)
    wines = excel_data.to_dict(orient='records')

    collection_of_wine = collections.defaultdict(list)

    for wine in wines:
        wine['Цена'] = int(wine['Цена'])
        collection_of_wine[wine['Категория']].append(wine)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        years_from_foundation=years_from_foundation,
        wines=collection_of_wine,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
