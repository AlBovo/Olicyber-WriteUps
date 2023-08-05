#!/usr/bin/env python3
from pwn import *

if args.REMOTE:
    p = remote('keygenme.challs.olicyber.it', 10017)
else:
    p = process('./keygenme')

def pairStrings(a2, a3): # a1, a2, a3 = char arrays, a4 = int
    result = [""] * 16
    v2, v3 = 0, 0
    for i in range(16):
        if i % 2 == 0:
            result[i] = a2[v2]
            v2 += 1
        else:
            result[i] = a3[v3]
            v3 += 1

    return "".join(i for i in result)

def makeSerial(user):
    result = ""
    result += pairStrings(user[18:], user[9:])
    result += pairStrings(user, user[18:])
    result += pairStrings(user[9:], user)
    return result
    


p.recvuntil(b'User id: ')
userID = p.recvuntil(b'\n').strip().decode()
userID = [i for i in userID]
key = makeSerial(userID)
print(key)
p.recv()
p.sendline(key)
p.interactive()
