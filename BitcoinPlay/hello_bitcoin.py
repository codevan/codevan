#!/usr/bin/env/ python
'''
Title - Hello Bitcoin
'''

# Import bitcoin
from bitcoin import *

my_private_key = random_key()
print("Private Key: %s\n" % my_private_key)

# Generate Public Key:
my_public_key = privtopub(my_private_key)
print("Public Key: %s\n" % my_public_key)

# Create Bitcoin Address:
my_bitcoin_key = pubtoaddr(my_public_key)
print("Bitcoin Address Key %s\n" % my_bitcoin_key)

