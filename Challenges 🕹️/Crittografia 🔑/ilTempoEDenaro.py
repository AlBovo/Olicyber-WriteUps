#!/usr/bin/env python3
from Crypto.Util.number import long_to_bytes
from tqdm import tqdm
from pwn import *

flag = [0] * 200
while True:
    r = remote("time.challs.olicyber.it", 10505)
    for i in tqdm(range(200)): # size della flag in binario
        if flag[i] == 1:
            continue
        r.recvuntil(b"> ")
        r.sendline(b"1")
        r.recvuntil(b"? ")
        r.sendline(str(i).encode())
        
        f = r.recvline().decode().strip()
        try:
            bytes.fromhex(f)
        except:
            flag[i] = 1
    r.close()
    
    binf = int("".join(map(str, flag)), 2)
    flagf = long_to_bytes(binf)
    print(flagf)
    if b'flag{' in flagf:
        input() # decidi se continuare o no