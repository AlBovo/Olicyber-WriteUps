#!/usr/bin/env python3
from Crypto.Cipher import AES
from hashlib import sha256
from pwn import *

r = remote("2fa.challs.olicyber.it", 12206)

def expand_pin(pin):
    return sha256(pin).digest()[:16]

r.recvuntil(b"\n\n")
r.sendline(b'3')
r.recvuntil(b'admin:')
token = r.recvline().strip().decode()
print(token)
k1, k2 = b"", b""

k1s = {}
for i in range(1000000):
    pin = str(i).zfill(6).encode()
    c1 = AES.new(expand_pin(pin), AES.MODE_ECB)
    k1s[c1.encrypt(b"donttrustgabibbo")] = pin

for i in range(1000000):
    pin = str(i).zfill(6).encode()
    c2 = AES.new(expand_pin(pin), AES.MODE_ECB)
    if c2.decrypt(bytes.fromhex(token)) in k1s:
        k1, k2 = pin, k1s[c2.decrypt(bytes.fromhex(token))]
        break

r.recvuntil(b"\n\n")
r.sendline(b'2')
r.recvuntil(b': ')
r.sendline(b'admin')
r.recvuntil(b': ')
r.sendline(k1)
r.recvuntil(b': ')
r.sendline(k2)
r.recvline()

flag = r.recvline()
print(flag.decode().strip())