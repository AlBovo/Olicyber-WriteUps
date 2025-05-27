#!/usr/bin/env python3
from z3 import *
flag = bytes.fromhex("7f1d26c428628a1dd436311d36b0054536f1a79c62f1f59c7b4a8ffc9ca7f19c31bbf16b1dc062e6b2")

s = Solver()
k = Int('k')
key = k * 2 + 1
f = [Int(f'f{i}') for i in range(len(flag))]

s.add((key * b'f'[0] + 1) % 256 == flag[0])
s.add((key * b'l'[0] + 1) % 256 == flag[1])
s.add((key * b'a'[0] + 1) % 256 == flag[2])
s.add((key * b'g'[0] + 1) % 256 == flag[3])
s.add((key * b'{'[0] + 1) % 256 == flag[4])

s.add(k > 0)
keys = []

if s.check() == sat:
    print("sat")
    m = s.model()
    k1 = m[k].as_long()
    key1 = k1 * 2 +1
    print(k1)

    for i in range(len(flag)): 
        for e in range(256):
            if (key1 * e + 1) % 256 == flag[i]:
                print(chr(e), end="")
    print()
else:
    print("unsat")
