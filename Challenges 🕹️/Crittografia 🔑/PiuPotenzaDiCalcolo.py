#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from libnum import factorial_mod
import os

def handle():
    flag = bytes.fromhex("b5609cfbad99f1b20ec3a93b97f379d8426f934ffcb77d83ea9161fefa78d243")
    for i in range(pow(10, 16)):
        keyExchanged = str(i) # hmmm
        encryptedFlag = decrypt(flag,keyExchanged)
        if b'flag' in encryptedFlag:
            print(encryptedFlag)
            return

def fakePadding(k):
    if (len(k) > 16):
        raise ValueError('La tua chiave è più lunga di 16 byte')
    else:
        if len(k) == 16:
            return k
        else:
            missingBytes = 16 - len(k)
            for i in range(missingBytes):
                k = ''.join([k,"0"])
            return k

def encrypt(f,k):
    key = bytes(fakePadding(k),"utf-8")

    cipher = AES.new(key, AES.MODE_ECB)
    encryptedFlag = cipher.encrypt(pad(f, AES.block_size))
    return encryptedFlag

def decrypt(f, k):
    
    key = fakePadding(str(k))
 
    chiave = bytes(key, "utf-8")
    cipher = AES.new(chiave, AES.MODE_ECB)
    decryptedFlag = cipher.decrypt(f)
    return decryptedFlag

if __name__ == "__main__":
    handle()