#!/usr/bin/env python3
import string
from pwn import remote

r = remote("geroglifici.challs.olicyber.it", 35000)
alph = str(string.ascii_letters + string.digits + '_{}!').encode()

r.recvuntil(b'recita ')
f = r.recvline().strip()
flag = [f[i:i+4] for i in range(0, len(f), 4)]
r.recvuntil(b'> ')
r.sendline(alph)
f = r.recvline().strip()
alph2 = [f[i:i+4] for i in range(0, len(f), 4)]
assert len(alph) == len(alph2)
m = {}
for i in range(len(alph)):
    m[alph2[i]] = alph[i]

n = []
for i in flag:
    print(chr(m[i]), end="")