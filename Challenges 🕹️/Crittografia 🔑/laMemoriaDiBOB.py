#!/usr/bin/env python3
from Crypto.Util.Padding import pad
from base64 import b64decode
import string
from pwn import *

r = remote("bob.challs.olicyber.it", 10602)
M = b'Bob: '
# buff = b''
# r.recvuntil(M)
# r.sendline(buff)
# f = r.recvline()

# for i in range(16):
#     r.recvuntil(b'1\n')
#     r.sendline(b'1')
#     r.recvuntil(M)
#     r.sendline(buff + b'a')
#     if len(r.recvline()) > len(f):
#         break
#     buff += b'a'
# # Trovato che len('Bob: ') + len(chat) è esattamente multiplo di 16
# assert len(buff) == 16

chat = b". Cosa ne pensi? Bob: Ok. Allora mi puoi dare la flag? Alice: Nah, ma ti pare? Sono studiata io... Bob: Ma seriamente, ti immagini se qualcuno riuscisse ad ottenere i nostri messaggi?"
alph = (string.ascii_letters + ' ' + string.digits + '?!:,.;_{}\'').encode('utf-8')
while True:
    flag = False
    if len(chat + b'0') % 16 == 6: # \n nel padding
        # consiglio di guessare il secondo carattere
        for i in alph:
            for e in alph:
                if 10 in [i, e]: # \n
                    continue
                r.recvuntil(M)
                test = pad(bytes([i, e]) + chat, 16)
                r.sendline(b'a' * 11 + test + b'a' * (len(chat) + 2))
                r.recvline()
                resp = b64decode(r.recvline())

                enc = resp[-len(test):][:16]
                guess = resp[16:32]

                print(enc.hex(), guess.hex(), bytes([i, e]))
                r.recvuntil(b'1\n')
                r.sendline(b'1')
                if enc == guess:
                    flag = True
                    chat = bytes([i, e]) + chat
                    print(chat)
                    break
            if flag:
                break
        assert flag
        continue

    for char in alph:
        if char == ord('\n'):
            continue            
        r.recvuntil(M)
        test = pad(bytes([char]) + chat, 16)
        r.sendline(b'a' * 11 + test + b'a' * (len(chat) + 1))
        r.recvline()
        resp = b64decode(r.recvline())

        enc = resp[-len(test):][:16]
        guess = resp[16:32]

        print(enc.hex(), guess.hex(), bytes([char]))
        if enc == guess:
            flag = True
            chat = bytes([char]) + chat
            print(chat)
            break
        r.recvuntil(b'1\n')
        r.sendline(b'1')
    if not flag:
        break
    r.recvuntil(b'1\n')
    r.sendline(b'1')
print(chat)