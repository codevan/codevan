#!/usr/bin/env/ python
'''
Title - get Exchange rates using blockchain.info

'''

# Import blockchain library
from blockchain import exchangerates

# get the bitcoin rates in various currencies

ticker = exchangerates.get_ticker()

print("Bitcoin Prices in various currencies:")
for k in ticker:
	print(k, ticker[k].p15min)

	
btc = exchangerates.to_btc('USD', 100)
print("\n\n100 USD in Bitcoin: %s " % btc)

btc = exchangerates.to_btc('GBP', 100)
print("\n100 GBP in Bitcoin: %s " % btc)
