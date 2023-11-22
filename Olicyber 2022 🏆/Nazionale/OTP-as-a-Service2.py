#!/usr/bin/env python3
from pwn import *

r = remote("otp2.challs.olicyber.it", 12306)

r.recvuntil(b'connessione\n')
l = [500 for i in range(71)]
for i in range(4000):
    r.sendline(b'e')
    f = r.recvline().decode().split('-')
    for e in range(len(f)):
        if int(f[e]) < l[e]:
            l[e] = int(f[e])

print(''.join([chr(i) for i in l]))