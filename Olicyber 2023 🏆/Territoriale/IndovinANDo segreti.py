from pwn import *
from Crypto.Util.number import *
r = remote("segreto.challs.olicyber.it", 33000, timeout=100000)
r.recv(1000)
for i in range(10):
    maxi = -1
    r.recv(1000)
    for e in range(256):
        r.sendline(str(e).encode())
        f = r.recvline(True)
        print(f)
        maxi = max(maxi, int(f.decode().replace(">", "").strip(), 16))
    r.recv(100)
    r.sendline(b"g")
    r.recv(1000)
    r.sendline(long_to_bytes(maxi).hex().encode())
print(r.recv(100).decode())