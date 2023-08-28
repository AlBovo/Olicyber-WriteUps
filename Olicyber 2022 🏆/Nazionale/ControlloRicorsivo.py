#!/usr/bin/env python3
from pwn import remote, args, process
from z3 import *
from string import printable

if args.REMOTE:
    p = remote("crc.challs.olicyber.it", 12201)
else:
    p = process("./controllo_ricorsivo_circa")

def HIBYTE(i):
    return (i >> 8) & 0xff

def crc16(string) -> int:
    pos = 0
    v6, i = 0, -1 # int8, int16

    while pos < len(string):
        v1 = string[pos]
        v6 = ((HIBYTE(i) ^ v1) >> 4) ^ HIBYTE(i) ^ v1
        i = (32 * v6) ^ (v6 << 12) ^ (i << 8) ^ v6
        pos += 1
    return i & ((1 << 16)-1)

assert crc16(b"fsacagsacaz") == 0x963c # calculated with the original binary
key = b""
def find(string):
    global key
    if len(string) == 30:
        return
    if crc16(string) == 0xE05B:
        key = string
        return
    for c in printable:
        find(string + c.encode())
        if key != b'':
            return
        
find(b'')
p.recvuntil(b"password: ")
p.sendline(key)
p.interactive()