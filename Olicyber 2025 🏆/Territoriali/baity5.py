#!/usr/bin/env python3
from pwn import *

context.terminal = ('kgx', '-e')
context.binary = elf = ELF('./baity5')
p = gdb.debug(elf.path, '''
        b *main+105
        c
    ''')

print("Watch the rsp")
p.interactive()
