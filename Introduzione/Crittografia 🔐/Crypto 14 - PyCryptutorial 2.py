#!/usr/bin/env python3
import re
from pwn import *
from Crypto.Hash import SHA3_384, SHA224, HMAC
from Crypto.PublicKey import DSA
from Crypto.Random import *
from Crypto.Util.number import *

r = remote("cr14.challs.olicyber.it", 30007)
r.recv(1000)
msg = b"hash_me_pls"
h = SHA3_384.new()
h.update(msg)
r.sendline(str(h.hexdigest()).encode())
r.recvuntil(b"'")
secret = bytes.fromhex(r.recvuntil(b"'").decode().replace("'", ""))
h = HMAC.new(secret, digestmod=SHA224)
r.recv(1000)
msg = "La mia integrità è importante!".encode()
h.update(msg)
r.sendline(str(h.hexdigest()).encode())
r.recvuntil(b"'")
key = r.recvuntil(b"'").replace(b"'", b"").decode()
r.recvuntil(b'\n')
print(key)
d = DSA.import_key(bytes.fromhex(key))
for i in range(3):
    f = r.recvuntil(b"? ").decode()
    print(f)
    if "p" in f:
        r.sendline(str(d.p).encode())
    elif "q" in f:
        r.sendline(str(d.q).encode())
    elif "g" in f:
        r.sendline(str(d.g).encode())
    elif "x" in f:
        r.sendline(str(d.x).encode())
    else:
        r.sendline(str(d.y).encode())
r.recvuntil(b"\n\n")
frase = r.recv(100).decode()
print(frase)
pattern = r'\b(\d+)\s*bit\b'
match = re.search(pattern, frase)
r.sendline(str(getPrime(int(match.group(1)))).encode())
r.recvuntil(b"= ")
f = int(r.recvuntil(b"\n").decode().strip())
r.recvuntil(b"(si/no)?")
r.sendline(b"si" if isPrime(f) else b"no")
r.interactive()
