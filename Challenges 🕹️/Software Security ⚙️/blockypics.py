#!/usr/bin/env python3
from pwn import *
from libdebug import debugger

d = debugger('./blockypics')
r = d.run()
bp = d.breakpoint('encryptCBC', hardware=True, file="binary")
d.cont()

while True:
    print(r.recvuntil(b'***\n'))
    print("Key: ", d.memory[int(d.regs.rdi), 0x20])
    print("IV: ", d.memory[int(d.regs.rdx), 0x10])
    if not bp.hit_on(d):
        print("porcoddio")
    d.cont()