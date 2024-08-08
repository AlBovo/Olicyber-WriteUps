#!/usr/bin/env python3
from pwn import *
from z3 import *

r = remote('chooseyourotp.challs.olicyber.it', 38302)

flag = 0
l = 0
for i in range(2, 420):
    nums = {1 : 0, 0 : 0}
    for e in range(3):
        r.recvuntil(b'> ')
        r.sendline(str(2**i))
        n = (int(r.recvline().strip().decode()) & (2**i)) >> i
        nums[n] = nums.get(n, 0) + 1
    g = 0
    k = 0
    print(i, nums)
    for e in nums:
        if nums[e] >= g:
            g = nums[e]
            k = e
    flag += k << i
    if k == 0:
        l += 1
        if l > 100:
            break
    else:
        l = 0
print(hex(flag))
print(flag.to_bytes((flag.bit_length() + 7) // 8, byteorder='big').decode())
