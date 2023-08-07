#!/usr/bin/env python3
import random

flagEncrypted = "088596df93697e62d71cb143352ccb45be15463219c6cc917f9be83c1aa1f7d0217b4586c1058009"

def find_key(flag):
    for i in range(256):
        ciphertext = []
        random.seed(i)

        for c in flag:
            encrypted_char = c ^ random.randint(0, 255)
            ciphertext.append(encrypted_char)
        if "088596df93" in bytes(ciphertext).hex(): # 088596df93 == flag{ encoded in hex
            return i

def decrypt(key):
    flag = []
    random.seed(key)

    for c in bytes.fromhex(flagEncrypted):
        flag.append(c ^ random.randint(0, 255))

    return bytes(flag).decode()

key = find_key(b"flag{")
print(key)
print(decrypt(key))
