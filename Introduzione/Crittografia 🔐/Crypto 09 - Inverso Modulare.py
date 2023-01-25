from pwn import *
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

r = remote("crypto-09.challs.olicyber.it", 30002)
r.recvuntil(b"= ")
a = int(r.recvuntil(b",").decode().replace(",",""))
r.recvuntil(b"= ")
b = int(r.recvuntil(b",").decode().replace(",",""))
gcd, x, y = extended_gcd(a, b)
r.sendline(str(x).encode())
r.recv(1000)
r.sendline(str(y).encode())
r.recvuntil(b"\n\n")
f = r.recv(100).split(b" ")
try:
    pow(int(f[0].decode()), -1, int(f[4].decode().replace("?",""))) # cambia i valori tranne -1
    r.sendline(b"si")
except:
    r.sendline(b"no")
r.recv(100)
r.recvuntil(b"\n\n")
f = r.recv(100).decode().split(" ")
r.sendline(str(pow(int(f[4]), -1, int(f[6].replace("?","")))).encode())
print(r.recv(100))