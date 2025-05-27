#!/usr/bin/env python3
from pwn import *
from Crypto.Util.number import *

r = remote("segreto.challs.olicyber.it", 33000)
r.recvuntil(b"flag!\n")

for i in range(10):
    maxi = 0
    f = r.recvuntil(b"10\n")
    print(i, f)
    #assert(ord(str(i+1)) == f[6]) esplode con il round 10
    for e in range(30):
        r.recv(100)
        try:
            r.sendline(str(e).encode())
        except:
            print(e-1, "error")
        f = r.recvuntil(b"\n").decode().replace(">", "").strip()
        #print(bin(int(f, 16)))
        maxi |= int(f, 16)
        #print(e, bin(maxi))
    r.recv(100)
    r.sendline(b"g")
    print(r.recv(1000))
    r.sendline(long_to_bytes(maxi).hex().encode())
print(r.recv(100).decode())
