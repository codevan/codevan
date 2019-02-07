#!/usr/bin/env/ python
'''
Title - Create multi-signature address
'''

# Import bitcoin
from bitcoin import *

my_private_key1 = random_key()
my_private_key2 = random_key()
my_private_key3 = random_key()
print("Private Key1: %s\n" % my_private_key1)
print("Private Key2: %s\n" % my_private_key2)
print("Private Key3: %s\n" % my_private_key3)
print('\n');

# Generate Public Key:
my_public_key1 = privtopub(my_private_key1)
my_public_key2 = privtopub(my_private_key2)
my_public_key3 = privtopub(my_private_key3)
print("Public Key1: %s\n" % my_public_key1)
print("Public Key2: %s\n" % my_public_key2)
print("Public Key3: %s\n" % my_public_key3)
print('\n');

# Create Multi-Sig Address:
my_multi_sig = mk_multisig_script(my_public_key1, my_public_key2, my_public_key3, 2, 3)
my_multisig_address = scriptaddr(my_multi_sig)
print("Multi Signature Address %s\n" % my_multisig_address)

