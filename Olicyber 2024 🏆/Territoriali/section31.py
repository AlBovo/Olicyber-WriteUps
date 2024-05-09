#!/usr/bin/env python3
from pwn import *

exe = ELF('./section31', checksec=False)

for i in exe.sections:
    name = i.name
    if name.startswith('flag'):
        print(name.split('_')[2], end='')
print()
