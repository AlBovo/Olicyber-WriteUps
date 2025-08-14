#!/usr/bin/env python3
from hashlib import sha512

def xor(a, b):
    return bytes(c ^ d for c, d in zip(a, b))

flag = bytes.fromhex("2CE4190BDF7C920301217B56B11F067FD361BB2F11B04E7B9A75912B16ADB5AF96E00ED7ECBCB1FC5CF80837AC4F40D181C0CDF9B8167CE2F982AC6A6F9035F2")
tung = sha512(b'tung tung tung sahur VS cappuccino assassino').digest()
flag = xor(flag, tung)

flag = [chr(flag[i] ^ 0x20) if i % 2 == 0 else chr(flag[i]) for i in range(len(flag))]
print(''.join(flag))
