#!/usr/bin/env python3
from pwn import *
from z3 import *
from sympy.ntheory import discrete_log
import re, math

r = remote("crypto-12.challs.olicyber.it", 30005)
r.recv(1000)
r.sendline(b"p-1")
r.recvuntil(b"\n\n")
frase = r.recv(1000).decode()
print(frase)
pattern = r"logaritmo discreto di (\d+) in base (\d+) \(mod (\d+)\)"
match = re.search(pattern, frase)
r.sendline(str(int(math.log(int(match.group(1)), int(match.group(2))))).encode())
r.recvuntil(b"\n\n")
frase = r.recv(1000).decode()
pattern = r"logaritmo discreto di (\d+) in base (\d+) \(mod (\d+)\)"
match = re.search(pattern, frase)
r.sendline(str(discrete_log(int(match.group(3)), int(match.group(1)), int(match.group(2)))).encode())
frase = r.recvuntil(b"?").decode()
#print(frase)
pattern = r"p = (\d+), g = (\d+).\nLa mia chiave pubblica è (\d+)"
match = re.search(pattern, frase)
p = int(match.group(1))
g = int(match.group(2))
c = int(match.group(3))
b = 15
r.sendline(str(pow(g, b, p)).encode())
r.sendline(str(pow(c, b, p)).encode())
r.interactive()
