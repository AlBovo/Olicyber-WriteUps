#!/usr/bin/env python3
from pwn import *
import re

REGEX = r'ptm{.*}'
r = remote("transfers-notes.challs.olicyber.it", 11306)

def getListTransactions(usr):
    r.sendline(b'5')
    r.recvuntil(b': ')
    r.sendline(usr.encode())
    r.recvuntil(b'[description]\n')
    trans = r.recvuntil(b'\n\n')

    return trans.split()

r.recvuntil(b'> ')
key = None
trans = getListTransactions("Admin")

for i in range(1, len(trans), 2):
    data = bytes.fromhex(trans[i].decode())
    if key == None:
        for e in range(256):
            f = xor(data, bytes([e]))
            if b' <- ' in f:
                key = bytes([e])
                break
    f = xor(data, key).decode()
    print(f[f.index('|'):])
