#!/usr/bin/env/ python

# Import blockchain library
from blockchain import statistics

# get the stats object
stats = statistics.get()

print("Bitcoin Trade volume: %s\n" % stats.trade_volume_btc)

print("Bitcoin Mined: %s\n" % stats.btc_mined)


print("Bitcoin market price: %s\n" % stats.market_price_usd)