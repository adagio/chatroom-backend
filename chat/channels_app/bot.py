import requests
from io import StringIO
import csv


def get_stock_quote(stock_code):
    if len(stock_code) > 0:
        try:
            response = requests.get(f'https://stooq.com/q/l/?s={stock_code}&f=sd2t2ohlcv&h&e=csv')
            f = StringIO(response.text)
            cr = csv.DictReader(f)
            row = next(cr)
            return '{} quote is {} per share'.format(row['Symbol'], row['Close'])
        except:
            pass
    return "Oh, You misspelled somewhere!"
