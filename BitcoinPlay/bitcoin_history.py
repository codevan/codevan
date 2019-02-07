#!/usr/bin/env/ python
'''
Title - Bitcoin Transaction History

Demostrates listing history of a bitcoin address fromm blockchain.info/com
'''

# Import bitcoin
from bitcoin import *

#View address transaction history
## Notes this block #548112 contains a 4,999BTC transaction ($53Million)
### https://www.blockchain.com/btc/block/00000000000000000010c8a2004f9a3725d98f310aef2b487037f684ae1e0d80
a_valid_bitcoin_address = '331Zw8ZMo6fKm3CKbvofiRQdx8sgNAtWYJ'
print(history(a_valid_bitcoin_address))

