#!/usr/bin/env python3
from pwn import *
from Crypto.Util.number import *
from z3 import *

risp = 'Nope!'
 
while 'Nope!' in risp:
    if args.REMOTE:
        p = remote('cryptorland.challs.olicyber.it', 10801)
    else:
        p = process('./challenge.py')

    n = []
    for _ in range(10):
        n.append(int(p.recvuntil(b'\n').decode()))
        #print(p.recvline())

    sol = BitVec('sol', 8 * 12)
    s = Solver()
    mini, maxi = 0, bytes_to_long(b'\xff' * 12)//2
    for i in n:
        x = BitVec(f'sol{str(i)}', 8 * 12)
        if mini <= i <= maxi:
            s.add(sol & x == i)
        else:
            s.add(sol | x == i)
    print(s.check())
    try:
        m = s.model()
        t = m[sol].as_long()
        p.recvuntil(b'? ')
        p.sendline(str(t).encode())
        risp = p.recv().decode()
        print(risp)
    except:
        pass
    p.close()
