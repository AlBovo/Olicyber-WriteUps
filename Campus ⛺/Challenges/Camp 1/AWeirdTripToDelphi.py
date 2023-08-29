#!/usr/bin/env python3
from pwn import remote, xor
import re

REGEX = r'flag{.*?}'.encode()

r = remote("trip-to-delphi.challs.olicyber.it", 34007)
r.recvuntil(b'iv.hex() = \'')
iv = r.recvuntil(b'\'', True)
r.recvuntil(b'enc_flag.hex() = \'')
enc_flag = r.recvuntil(b'\'', True)

iv_test = bytes.fromhex(iv.decode())
flag_t = [enc_flag[i:i+32] for i in range(0, len(enc_flag), 32)]
flag_t += [iv] + flag_t
flag_t = b''.join(flag_t)

r.recvuntil(b'iv (hex): ')
r.sendline(iv)
r.recvuntil(b'ciphertext (hex): ')
r.sendline(flag_t)

r.recvuntil(b'oracle(ciphertext, iv).hex() = \'')
flag = r.recvuntil(b'\'', True)
flag = bytes.fromhex(flag.decode())[7:]
flag = xor(flag[0:16], flag_t[0]) + flag[16:]
flag = re.findall(REGEX, flag)[0]
print(flag.decode())