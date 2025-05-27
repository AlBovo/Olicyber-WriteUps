#!/usr/bin/env python3
from pwn import *

g = gdb.debug('./ghost', '''
        b *0x4015A9
        continue
    ''')
g.interactive() # la flag è in RDI
