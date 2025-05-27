#!/usr/bin/env python3
from pwn import *
from sympy import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import long_to_bytes

p = 1 << 1024
'''
while True:
    if isprime((p-1)//2):
        break
    p = nextprime(p)
'''
p = 179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624225795083 # precalcolato
g, b = 5, 15
r = remote("crypto-13.challs.olicyber.it", 30006)
r.recv(1000)
r.sendline(str(p).encode())
r.recv(1000)
r.sendline(str(g).encode())
r.recv(1000)
r.sendline(str(pow(g, b, p)).encode())
r.recvuntil(b". ")
A = int(r.recv(1000).decode().replace("\n", ""), 16)
r.recvuntil(b"IV: ")
shared = pow(A, b, p)
IV = bytes.fromhex(r.recvuntil(b"\n").decode().replace("\n",""))
msg = bytes.fromhex(r.recv(1000).decode().replace("msg: ", "").strip())
flag = AES.new(long_to_bytes(shared)[:16], AES.MODE_CBC, IV).decrypt(msg)
print(flag.decode().replace("\r",""))
