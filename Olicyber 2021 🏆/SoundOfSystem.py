#!/usr/bin/env python3
from Crypto.Cipher import AES
from pwn import remote
import os, re

seed = os.urandom(16)

def xor(a, b):
    return bytes(x^y for x,y in zip(a,b))

def pad(m):
    if len(m)%48 == 0:
        return m
    return m + bytes([48-len(m)%48])*(48-len(m)%48)

class Hash(object):
    def __init__(self, msg):
        self.seed = seed
        self.msg = pad(msg)

    def hash(self):
        cipher = AES.new(self.seed, AES.MODE_ECB)
        blocks = [self.msg[i:i+16] for i in range(0, len(self.msg), 16)]
        prev = bytes(16)
        res = bytes(16)

        for b in blocks:
            res = xor(xor(prev, res), cipher.decrypt(b)) # cbc tarocco wtf
            prev = b 

        # prima res = cipher.decrypt(blocks[0])
        # prima prev = blocks[0] = (show_flag''''''')
        # seconda res = cipher.decrypt(blocks[1]) ^  cipher.decrypt(blocks[0]) ^ blocks[0]
        # seconda prev = blocks[1] = ('''''''''''''''')
        # terza res = cipher.decrypt(blocks[2]) ^  cipher.decrypt(blocks[1]) ^  cipher.decrypt(blocks[0]) ^ blocks[0] ^ blocks[1]
        # res = cipher.decrypt("show_flag'''''''") ^ "show_flag'''''''" ^ "''''''''''''''''"

        return res.hex()

payload = b"'" * 16 + b'show_flag' + b"'" * (16 - len(b"show_flag") + 16)
blacklist = [pad(b"show_flag")]
assert pad(payload) not in blacklist
assert Hash(b'show_flag').hash() == Hash(payload).hash()

r = remote("soundofsystem.challs.olicyber.it", 15000)
r.recvuntil(b"> ")
r.sendline(payload)
flag = re.findall(r"flag{.*?}", r.recvuntil(b'to do!').decode())[0]
print(flag)