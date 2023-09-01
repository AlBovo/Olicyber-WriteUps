#!/usr/bin/env python3
import string

enc_flag = bytes.fromhex("7dc0bc0397aa6f7c412f99720039840e6e1749072f9e350189c14cc12cff")
f = b'flag{'
bits = [(enc_flag[i] ^ f[i]) for i in range(len(f))]

state = [] # 40 bit sicuri
states = [] # tutte le possibili combinazioni dei seguenti 16 bit

for i in bits:
    f = bin(i)[2:].rjust(8, '0')
    state += [int(j) for j in f]

for i in range(256):
    for e in range(256):
        states += [state + 
            [int(j) for j in bin(enc_flag[len(f)]^i)[2:].rjust(8, '0')] +
            [int(j) for j in bin(enc_flag[len(f)+1]^e)[2:].rjust(8, '0')]
        ]

for i in states:
    assert len(i) == 56

def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

class LFSR(object):
    def __init__(self, s):
        self.s = list(map(int, s))

    def gen_stream(self, n):
        out = []
        for i in range(n):
            out.append(self.s[0])
            self.s = self.s[1:] + [self.s[0]^self.s[3]^self.s[7]^self.s[9]]
        return out

for i in states:
    L = LFSR(i)
    k = b''
    for e in range(len(enc_flag)):
        k += bytes([int("".join(str(x) for x in L.gen_stream(8)), 2)])
    
    flag = xor(enc_flag, k)
    if b'flag{' in flag and all(c in string.printable.encode() for c in flag):
        print(flag)
        break