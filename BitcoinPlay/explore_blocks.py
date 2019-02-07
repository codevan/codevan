#!/usr/bin/env/ python

# Import blockchain library
from blockchain import blockexplorer	#uses blockchain.info api

# get the stats object
block = blockexplorer.get_block('00000000000000000010c8a2004f9a3725d98f310aef2b487037f684ae1e0d80')

print("Block fee: %s\n" % block.fee)
print("Block size: %s\n" % block.size)
#print("Block transactions: %s\n" % block.transactions)

block = blockexplorer.get_latest_block()
print("Latest block : %s\n" % block)
