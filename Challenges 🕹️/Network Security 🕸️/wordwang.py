#!/usr/bin/env python3
from pwn import *

while True:
    r = remote("wordwang.challs.olicyber.it", 10601)
    r.recvline()
    if "speech" in r.recvline().decode():
        r.sendline(b'?SPEECH!')
        r.interactive()
        exit(0)
    r.close()
