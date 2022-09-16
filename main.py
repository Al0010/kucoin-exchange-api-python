from kucoin.client import Client
import pandas as pd
import datetime

api_key = "YOUR API KEY"
api_secret = "YOUR API SECRET"
api_passphrase = "YOUR API PASSWORD"
client = Client(api_key, api_secret, api_passphrase)

# Get currencies
listcurrencies = client.get_currencies()

#print(listcurrencies)

# Get markets
listmarkets = client.get_markets()

#print(listmarkets)

# Get single ticker: ETH-USDT
ticker = client.get_ticker("ETH-USDT")

#print(ticker)

# Get all tickers
symbols = client.get_symbols()
specificSymbols = pd.DataFrame.from_dict(symbols)

#specificSymbols.head()
#print(symbols)
#print(specificSymbols)

# Get time for the single ticker
ticker_time = datetime.datetime.fromtimestamp(ticker['time'] / 1e3)

#print(ticker_time)

# Get a list of all bids and asks aggregated by price for a symbol !!!!

#This call is generally used by professional traders because 
#it uses more server resources and traffic, and Kucoin has strict access frequency control.
fullOrderBook = client.get_full_order_book("ETH-USDT")

#print(fullOrderBook)

# Get a list of bids and asks aggregated by price for a symbol !!!!
#Returns up to 20 or 100 depth each side. Fastest Order book API.
orderBook = client.get_order_book("ETH-USDT")

#print(orderBook)
