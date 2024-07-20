#!/usr/bin/env python3
from base64 import b64encode, b64decode
from pwn import *
import re

FLAG = r'flag{.*}'
r = remote("flip.challs.olicyber.it", 10603)

z = '{"admin":  true,'
t = '{"admin": false,'
xored = xor(z.encode(), t.encode())

r.recvuntil(b'!!!\n')
r.sendline(b'1')
r.recvuntil(b': ')
r.sendline(b'Dammi la flaaag!')
r.recvuntil(b': ')
msg = r.recvline().strip()
r.recvuntil(b': ')
iv = b64decode(r.recvline().strip().decode())
iv = xor(iv, xored)
iv = b64encode(iv)

r.recvuntil(b'!!!\n')
r.sendline(b'2')
r.recvuntil(b': ')
r.sendline(msg)
r.recvuntil(b': ')
r.sendline(iv)

data = r.recvuntil(b'!!!\n').decode()
flag = re.findall(FLAG, data)[0]
print(flag)
