#!/usr/bin/env python3
from pwn import *

p = process("./runme")
p.recvline()
p.sendline(b'33')
print(p.recv().decode().strip())