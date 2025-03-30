#!/usr/bin/env python3
from pwn import *
from ctypes import CDLL

CDLL = CDLL('/usr/lib/libc.so.6')
CDLL.srand(0x1337)

li = [(i % 5, CDLL.rand()) for i in range(500)][::-1]

def xor(a, b):
    res = []
    for i in a:
        res.append((i ^ (b & 0xff)) & 0xff)
    return bytes(res)

def sub(a, b):
    res = []
    for i in a:
        res.append((i - (b & 0xff)) & 0xff)
    return bytes(res)

def add(a, b):
    res = []
    for i in a:
        res.append((i + (b & 0xff)) & 0xff)
    return bytes(res)

def rl(a, b):
    res = []
    assert len(a) == 36
    for i in range(len(a)):
        res.append(a[(i + b) % len(a)])
    return bytes(res)

def rr(a, b):
    res = []
    assert len(a) == 36
    for i in range(len(a)):
        res.append(a[(i - b + 36) % len(a)])
    return bytes(res)

key = bytes.fromhex('1f84e6290b29a50954607fb2ad6615796a522d688d89acffe95a771ce9ba0d12b0288d7c')
assert len(key) == 36, len(key)

for i in range(500):
    curr = li[i]
    if curr[0] == 0:
        key = xor(key, curr[1])
    elif curr[0] == 1:
        key = sub(key, curr[1])
    elif curr[0] == 2:
        key = add(key, curr[1])
    elif curr[0] == 3:
        key = rr(key, curr[1])
    elif curr[0] == 4:
        key = rl(key, curr[1])
    else:
        exit(1)

key = key.hex()
r = remote("magicbb.challs.olicyber.it", 38050)
r.recvline()
r.sendline(key.encode())
print(r.recvline().decode().strip())
