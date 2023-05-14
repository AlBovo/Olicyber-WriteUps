#!/usr/bin/env python3

from z3 import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

''' da input '''
g = 126410689802884623988756200712033318972
A = 52231676617151166420364050960016472553
B = 9306272951250678880959738917375588033
iv = bytes.fromhex('39e9c1023681591d13604a1964cdf62f')
enc_flag = bytes.fromhex('66fc9e95577c38f8a2153e1e7e96be950c1eabd46d8b70a6304fd1b81b70be5f')

s = Solver()

def o(x, y):
    return x + y - 2*(x&y)

a, b = BitVecs('a b', 128)
s.add(A == o(g, a))
s.add(B == o(g, b))
s.add(o(a, B) == o(b, A))
print(s.check())
m = s.model()
a1, b1 = m[a].as_long(), m[b].as_long()
sharedAlice = o(a1, B)
sharedBob = o(b1, A)
print(sharedAlice, sharedBob)
assert sharedAlice == sharedBob
flag = AES.new(sharedAlice.to_bytes(16, "big"), AES.MODE_CBC, iv).decrypt(enc_flag)
print(unpad(flag, 16))
