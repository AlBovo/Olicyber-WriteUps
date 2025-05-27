#!/usr/bin/env python3
from Crypto.Cipher import AES
from pwn import xor, remote

t = bytes.fromhex("866bb5802051d56f37b1073a501b4afe4324424336ba60d4efe9af817b27a95a0f3adec8b809088bbaaebbfa0629c079")
iv = t[:16]
flag = [t[16:32],t[32:48]]

for i in flag:
    assert len(i) == 16
flagDecoded = ""
temp = iv
for i in range(2):
    r = remote("modes.challs.olicyber.it", 10802)
    r.recvuntil(b": ")
    r.sendline(flag[i].hex().encode())
    risp = bytes.fromhex(r.recvline().strip().decode())
    flagDecoded += xor(risp,temp).decode()
    temp = flag[i]
print(flagDecoded)