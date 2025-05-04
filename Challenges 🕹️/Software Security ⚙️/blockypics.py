#!/usr/bin/env python3
from ctypes import CDLL
from pwn import *
from Crypto.Cipher import AES
import re

lib = CDLL('/usr/lib/libc.so.6')

def init():
    lib.srand(0xE621)
    v0 = lib.rand()
    lib.srand(v0 % 10000)
    v1 = lib.rand()
    lib.srand(v1)
    v2 = lib.rand()
    lib.srand(v2)
    v3 = lib.rand()
    lib.srand(v3)

def gen1(src, a2):
    buf = bytearray(src)
    v2 = lib.rand()
    v4 = v2 % a2
    result = v2 // a2

    if a2 > 0:
        v5 = 0
        v6 = v4
        while v5 != a2:
            v7 = v6 + v5
            v8 = buf[v7 % a2]
            result = lib.rand() % 256
            buf[v5] = result ^ v8
            v5 += 1
    assert len(buf) == a2
    return bytes(buf)

def gen2(src, a2):
    buf = bytearray(src)

    if a2 > 0:
        for i in range(a2):
            v3 = buf[ lib.rand() % a2 ]
            rnd = lib.rand() % 256
            buf[i] = rnd ^ v3

    assert len(buf) == a2
    return bytes(buf)

def genkey(a1, a2):
    if lib.rand() & 1 != 0:
        return gen1(a1, a2)
    else:
        return gen2(a1, a2)


r = remote('blockypics.challs.olicyber.it', 10805)
r.recvline()

f = []
for i in range(5):
    r.recvline()
    f.append(bytes.fromhex(r.recvline().decode().strip()))
    
r = []
init()

for i in f:
    key = b'\0' * 0x20
    key = genkey(key, 0x20)
    iv = b'\0' * 0x10
    iv = genkey(iv, 0x10)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    r.append(cipher.decrypt(i))

r = r[:-4]
r = b''.join(r)
with open('out.png', 'wb') as f:
    f.write(r)