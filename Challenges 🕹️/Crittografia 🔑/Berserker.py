#!/usr/bin/env python3
from pwn import *
import string

def pad(m, l):
    if len(m) == l:
        return m
    return m.ljust(l, bytes([l-len(m)]))

r = remote('berserker.challs.olicyber.it', 10507)
alph = string.printable[:-5]

# TODO: there is a bug when the size of the flag is
# exactly (16*x)-1 es : 15, 31 ...
# the way I fixed is to just place the flag in the string and guess the char
flag = b''
while not flag.startswith(b'flag{'):
    r.recvuntil(b'> ')
    r.sendline(b'1')
    payload = b'a' * (5 + len(flag) + 1)

    r.recvuntil(b'? ')
    r.sendline(payload)
    r.recvuntil(b': ')
    c = bytes.fromhex(r.recvline().strip().decode())
    size = len(flag) // 16
    blocks = [c[i:i+16] for i in range(0, len(c), 16)]
    print(blocks, size)
    block = blocks[-size-1]
    iv_f = blocks[-size-2]
    iv = blocks[-1]
    assert len(iv_f) == len(iv) == len(block) == 16

    for i in alph:
        r.recvuntil(b'> ')
        r.sendline(b'2')
        payload = xor(xor(pad(i.encode() + flag[:15], 16), iv_f), iv).hex()
        r.recvuntil(b': ')
        r.sendline(payload.encode())
        r.recvuntil(b': ')
        f = r.recvline().strip()
        iv = bytes.fromhex(f[32:].decode())

        if bytes.fromhex(f[:32].decode()) == block:
            flag = i.encode() + flag
            break
    print(f'flag => {flag.decode()}')
