#!/usr/bin/env python3
from pwn import *
import math

r = remote("babyoracle.challs.olicyber.it", 12007)

r.recvuntil(b'n = ')
n = int(r.recvline().strip().decode())
r.recvuntil(b'flag = ')
enc = int(r.recvline().strip().decode())
r.recvuntil(b': ')
r.sendline(b'2')
num = int(r.recvline().strip().decode())
num = pow(num, 0x10001) - 2
p = math.gcd(n, num)
q = n // p
d = pow(0x10001, -1, (p-1)*(q-1))
flag = pow(enc, d, n)
print(flag.to_bytes(flag.bit_length() // 8 + 1))
