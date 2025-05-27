#!/usr/bin/env python3
from pwn import remote
from base64 import b64decode
from Crypto.Cipher import AES
import re

REGEX = r": [A-Za-z0-9+/=]*\n"

r = remote("corrupted.challs.olicyber.it", 10604)
g, p = b"1", b"ff"
r.recv()
r.sendline(g + b" " + p)
text = r.recvuntil(b'=\n').decode()
flag = b64decode(re.findall(REGEX, text)[0][2:-1].encode())
cipher = AES.new(int(1).to_bytes(16, 'big'), AES.MODE_ECB)
print(cipher.decrypt(flag).decode()[:-1])