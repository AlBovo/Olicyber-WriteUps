#!/usr/bin/env python3
from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime
import random, base64

flag = ""

def RSA(x: bytes) -> bytes:
    e = 65537
    random.seed(bytes_to_long(b"ptm{"))
    p = getPrime(1024, randfunc=random.randbytes)
    q = getPrime(1024, randfunc=random.randbytes)
    N = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return long_to_bytes(pow(bytes_to_long(x), d, N))

def rot13(x: bytes) -> bytes:
    return x.translate(bytes.maketrans(
        bytes([i for i in range(256)]),
        bytes([(i - 13) % 256 for i in range(256)])
    ))

possible_methods = [
    base64.b64decode,
    lambda x: x[::-1],
    RSA,
    rot13
]
while True:
    r = remote("magic-not-crypto.challs.olicyber.it", 11301)
    r.recvuntil(b"\n\n")
    steps = eval(r.recvuntil(b"]").decode())
    print(steps)
    if not 2 in steps or (steps[0] == 2 and not 2 in steps[1:]):
        r.recvline()
        flag = r.recvline().strip().decode()
        break
    r.recvall()
    r.close()

steps = steps[::-1]
flag = bytes.fromhex(flag)
for step in steps:
    flag = possible_methods[step](flag)
    
print(flag)