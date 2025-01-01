#!/usr/bin/env python3
from pwn import *

def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r

p = 5371695748955787613
data = b'admin=False&user=r'

BLOCK_LEN = 8
blocks = [data[i*BLOCK_LEN:(i+1)*BLOCK_LEN] for i in range(len(data)//BLOCK_LEN + 1)]
blocks_i = [int.from_bytes(block, 'big') for block in blocks]

print(blocks_i)

r = remote("notpoly.challs.olicyber.it", 35001)
r.recvuntil(b'> ')
r.sendline(b'2')
r.recvuntil(b'? ')
r.sendline(b'r')
f = int(r.recvline().decode().strip().split('.')[1])

a, b, c = blocks_i
c -= f
print(a, b, c)
q = tonelli(b**2 - 4*a*c, p)

x_1 = ((-b + q) * pow(2*a, -1, p)) % p
x_2 = ((-b - q) * pow(2*a, -1, p)) % p

class MAC():
    def __init__(self, key):
        self.k = int.from_bytes(key, byteorder="big")
        self.q = 5371695748955787613

    def _hash(self, data):
        blocks = [data[i*BLOCK_LEN:(i+1)*BLOCK_LEN] for i in range(len(data)//BLOCK_LEN + 1)]
        tag = 0
        for b in blocks:
            val = int.from_bytes(b, byteorder="big")
            tag = (tag*self.k + val) % self.q
        return tag

    def sign(self, msg):
        data = msg.encode()
        tag = self._hash(data)
        return f"{msg}.{tag}"

    def verify(self, cookie):
        data, tag = cookie.split(".")[:2]
        data = data.encode()
        tag = int(tag)
        return self._hash(data) == tag
    
mac1, mac2 = MAC(x_1.to_bytes(8, 'big')), MAC(x_2.to_bytes(8, 'big'))
f = 'admin=True&user=root'
sign1 = mac1.sign(f)
sign2 = mac2.sign(f)

print("Prova questi: ", sign1, sign2)
r.interactive()