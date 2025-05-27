#!/usr/bin/env python3
from pwn import xor

flag = b"\x57WTEZfXhBBWVTPPhjUeuPCVW"
key = bytes.fromhex("BD C3 B5 AC D5 D9 CD DB B5  B7 C9 E8 B5 BD 81 C7 D6 89 C4 DB BC 77 DD D4".replace(" ",""))
print(len(flag), len(key))
for i in range(len(flag)):
    print(chr(key[i] - flag[i]), end="")
