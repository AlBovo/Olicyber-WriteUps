from z3 import *
from pwn import *
from Crypto.Util.number import bytes_to_long

p = 290413720651760886054651502832804977189
pub_key = 285134739578759981423872071328979454683
c = bytes_to_long("get_flag".encode())
sign = Int("signature")
s = Solver()
s.add((pub_key * sign) % p == c)
s.check()
m = s.model()[sign].as_long()
r = remote("il-solito-servizio.challs.olicyber.it", 34006)
r.recv()
r.sendline(b"1")
r.recv()
r.sendline(str(m).encode())
r.recvuntil(b"flag!\n")
print(r.recvuntil(b"}").decode())