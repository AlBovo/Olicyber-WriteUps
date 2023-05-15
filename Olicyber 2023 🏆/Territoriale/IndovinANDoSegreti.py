from pwn import *
from Crypto.Util.number import *
r = remote("segreto.challs.olicyber.it", 33000)
r.recvuntil(b"flag!\n")
for i in range(10):
    maxi = -1
    f = r.recvuntil(b"10\n")
    print(f)
    assert(ord(str(i+1)) == f[6])
    for e in range(256):
        r.recv(100)
        try:
            r.sendline(str(e).encode())
        except:
            print(e-1)
        f = r.recvuntil(b"\n")
        #print(f)
        print(e)
        maxi = max(maxi, int(f.decode().replace(">", "").strip(), 16))
    r.recv(100)
    r.sendline(b"g")
    print(r.recv(1000))
    r.sendline(long_to_bytes(maxi).hex().encode())
print(r.recv(100).decode())