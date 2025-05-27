#!/usr/bin/env python3
from pwn import *

r = remote('spg.challs.olicyber.it', 38052)
r.sendlineafter(b'> ', b'1')
r.sendlineafter(b'Username? ', b'aa')
r.sendlineafter(b'> ', b'1')
r.sendlineafter(b'Username? ', b'aa;index0=0;index1=1;index2=2;index3=3\x01')
r.recvuntil(b'token: ')
t = r.recvline().strip()
t = t[:(16 + 48) * 2]

r.sendlineafter(b'> ', b'2')
r.sendlineafter(b'Token? ', t)
r.recvuntil('La tua passphrase è '.encode('utf-8'))
f = r.recvline().strip().decode().split('-')
print(''.join(f))