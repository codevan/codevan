#!/usr/bin/env/ python

# Import blockchain library
from blockchain import statistics

# Original block reward for miners was 50 BTC
start_block_reward = 50
# 210000 is around every 4 years with a 10 minute block interval
reward_interval = 210000


def max_money(a):
    multiplier = 1
    if a == "Satoshis":
        multiplier = 10**8
        
    # 50 BTC = 50 0000 0000 Satoshis
    current_reward = 50 * multiplier
    total = 0

    while current_reward > 0:
        total += reward_interval * current_reward
        current_reward /= 2
    return total

# get the stats object
stats = statistics.get()

btcmined = stats.btc_mined / 10000

percent_mined = (btcmined / max_money("Bitcoin")) * 100


print("Total SAT to ever be created:", max_money("Satoshis"), "Satoshis")
print("Total BTC to ever be created:", max_money("Bitcoin"), "Bitcoin")

print("Bitcoin Mined: %s (*10000)\n" % stats.btc_mined)

print("Percent bitcoins mined: %s", percent_mined)

