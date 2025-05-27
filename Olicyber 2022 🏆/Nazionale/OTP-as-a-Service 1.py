from pwn import *
from Crypto.Util.number import *
import time, random

t = int(time.time())-10
r = remote("otp1.challs.olicyber.it", 12304)
r.recv(1000)
r.sendline(b"e")
f = r.recvline().decode().replace("\n", "").split("-")
for i in range(len(f)):
    f[i] = int(f[i])
for i in range(0, 20):
    m = []
    random.seed(t+i)
    for e in f:
        s = random.randint(0,255)
        m.append(long_to_bytes(e+256-s).replace(b"\x01", b""))
    if m[0] == b"f":
        for i in m:
            print(i.decode(), end="")
        print()