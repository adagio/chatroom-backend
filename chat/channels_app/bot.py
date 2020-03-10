import requests
from io import StringIO
import csv
import sys


def get_stock(stock_code):
    response = requests.get(f'https://stooq.com/q/l/?s={stock_code}&f=sd2t2ohlcv&h&e=csv')
    f = StringIO(response.text)
    cr = csv.DictReader(f)
    row = next(cr)
    if (row['Date'] == 'N/D' and row['Close'] == 'N/D'):
        return f"stock_code {stock_code} is not defined"
    else:
        return f"{row['Symbol']} quote is {row['Close']} per share"


def get_stock_quote(stock_code):
    if len(stock_code) > 0:
        try:
            return get_stock(stock_code)
        except requests.exceptions.Timeout as err:
            # Maybe set up for a retry, or continue in a retry loop
            print(f"Timeout: {err}")
            return "Request timeout has ocurred"
        except requests.exceptions.RequestException as err:
            print(f"Connection Error: {err}")
            return "There was a connection error"
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return "Unexpected Error"
    return "Oh, You misspelled somewhere!"

