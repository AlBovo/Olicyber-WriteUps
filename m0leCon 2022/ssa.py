#!/usr/bin/env python3
from pwn import remote
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from sympy.ntheory import discrete_log

r = remote("ssa.challs.olicyber.it", 11302)

r.recvuntil(b"p = ")
g = 2
p = int(r.recvline().strip())
r.recvuntil(b"A = ")
A = int(r.recvline().strip())
r.recvuntil(b"B = ")
B = int(r.recvline().strip())

a = discrete_log(p, A, g)
key = int(pow(B, a, p)).to_bytes(16, 'little')
r.recvuntil(b'IV = ')
iv = bytes.fromhex(r.recvline().strip().decode())
cipher = AES.new(key, AES.MODE_CBC, iv)
r.recvuntil(b'Message = ')
message = bytes.fromhex(r.recvline().strip().decode())
flag = cipher.decrypt(message)
print(flag)