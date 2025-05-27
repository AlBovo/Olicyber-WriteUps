#!/usr/bin/env python3
from pwn import remote, xor
import os

r = remote("privateiv.challs.olicyber.it", 10021)

def encrypt(payload):
    r.recvuntil(b'> ')
    r.sendline(b'1')
    r.recvuntil(b'messaggio: ')
    r.sendline(payload.encode())
    r.recvuntil(b': ')
    encoded = r.recvline().strip().decode()
    return encoded

def decrypt(payload):
    r.recvuntil(b'> ')
    r.sendline(b'2')
    r.recvuntil(b'messaggio: ')
    r.sendline(payload.encode())
    r.recvuntil(b': ')
    encoded = r.recvline().strip().decode()
    return encoded

payload = os.urandom(47).hex()
encoded = bytes.fromhex(encrypt(payload))
flag = bytes.fromhex(decrypt(encoded[:16].hex() + '00' * 16 + encoded[:16].hex()))
print(len(flag))
print(xor(flag[:16], flag[32:]))
