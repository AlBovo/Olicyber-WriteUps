from pwn import *
r = remote("flagvault.challs.olicyber.it",34000)
r.recv()
r.sendline("49CMO:N?O2CD".encode())
print(r.recv())
