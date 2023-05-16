#!/usr/bin/env python3
from pwn import *
from z3 import *
import time

r = remote("crypto-10.challs.olicyber.it", 30003)
r.recvuntil(b"\n\n")
m = r.recvuntil(b"?").decode().split()

x = Int('x')
s = Solver()
mod, sol = 2, 4

for i in range(5):
    print(f"x % {m[mod]} = {m[sol]}")
    s.add(simplify(x % int(m[mod]) == int(m[sol])))
    mod += 5
    sol += 5
print(s.check())
me = s.model()
r.sendline(str(me[x].as_long() % int(m[-3])).encode())
r.interactive()
