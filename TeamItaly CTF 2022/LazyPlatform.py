#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
from randcrack import RandCrack
from pwn import *
import os

rc = RandCrack()

def split_bits(value, n=32):
    mask, parts = (1 << n) - 1, []
    while value:
        parts.append(value & mask)
        value >>= n
    return parts

'''
def remove_bits(value: int, n: int):
    return value & ((1 << (value.bit_length() - n)) - 1)

def get_last_n_bits(value: int, n: int):
    return (value >> (value.bit_length() - n)) & ((1 << n) - 1)
'''

r = remote('lazy-platform.challs.olicyber.it', 16004)

for i in range(624 // (8 + 4)): # tutti i bit necessari per predictare i numeri 'casuali'
    r.recvuntil(b'> ')
    r.sendline(b'1')
    r.recvuntil(b': ')
    r.sendline(os.urandom(8).hex().encode())
    r.recvuntil(b'Key:')

    key_bytes = bytes.fromhex(r.recvline().decode().strip())
    assert len(key_bytes) == 32
    key = int.from_bytes(key_bytes, "little")

    r.recvuntil(b'IV:')

    iv_bytes = bytes.fromhex(r.recvline().decode().strip())
    assert len(iv_bytes) == 16
    iv = int.from_bytes(iv_bytes, "little")

    for i in split_bits(key):
        rc.submit(i)
    for i in split_bits(iv):
        rc.submit(i)

# provo se funziona il generatore
r.recvuntil(b'> ')
r.sendline(b'1')
r.recvuntil(b': ')
r.sendline(os.urandom(8).hex().encode())
r.recvuntil(b'Key:')
key_bytes = bytes.fromhex(r.recvline().decode().strip())
key_gen = rc.predict_getrandbits(32 * 8).to_bytes(32, "little")
print(key_bytes.hex(), key_gen.hex())
assert key_bytes == key_gen
r.recvuntil(b'IV:')
iv_bytes = bytes.fromhex(r.recvline().decode().strip())
iv_gen = rc.predict_getrandbits(16 * 8).to_bytes(16, "little")
print(iv_bytes.hex(), iv_gen.hex())
assert iv_bytes == iv_gen

# cerco di decryptare la flag
r.recvuntil(b'> ')
r.sendline(b'3')
r.recvuntil(b'Ciphertext:')
flag = bytes.fromhex(r.recvline().decode().strip())

key = rc.predict_getrandbits(32 * 8).to_bytes(32, "little")
iv = rc.predict_getrandbits(16 * 8).to_bytes(16, "little")

ciphertext = AES.new(key, AES.MODE_CBC, iv).decrypt(flag)
print(ciphertext)