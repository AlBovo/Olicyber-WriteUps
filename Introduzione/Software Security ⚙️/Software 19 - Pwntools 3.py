from pwn import *
e = ELF("./sw-19")
r = remote("software-19.challs.olicyber.it", 13002)
r.recvuntil(b" ...")
r.sendline()
for _ in range(20):
    #r.interactive()
    r.recvuntil(b" ")
    fun = r.recvuntil(b": ").decode().replace(": ","")
    r.sendline(hex(int(e.sym[fun])).encode())
print(r.recv(100).decode())
