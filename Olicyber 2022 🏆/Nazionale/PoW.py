#!/usr/bin/env python3
from pwn import args, remote
from hashlib import sha256
import json, os

if args.REMOTE:
    file = open("precalc.json","r").read()
    data = json.loads(file)
    r = remote("pow.challs.olicyber.it", 12209)
    while True:
        r.recvuntil(b'with ')
        f = r.recvline().strip().decode()
        r.sendline(data[f])
else:
    data = {}
    while len(data) < pow(16,6):
        m = os.urandom(8)
        h = sha256(m).hexdigest()
        data[h[:6]] = m.hex()
    file = open("precalc.json","w")
    file.write(json.dumps(data))