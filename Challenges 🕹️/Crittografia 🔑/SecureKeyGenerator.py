from datetime import datetime
from Crypto.Util.number import *
from hashlib import sha256
from itertools import cycle
import random

# 2021-03-21 17:37:40
def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')

def generate_secure_key():
    time = int(datetime.timestamp(datetime(2021, 3, 21, 17, 37, 40)))
    h = sha256(int_to_bytes(time)).digest()
    seed = int_from_bytes(h[32:])
    key = h[:32]
    random.seed(seed)
    for _ in range(32):
        key += bytes([random.randint(0, 255)])
    return key

def xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, cycle(ba2))])

#sys.set_int_max_str_digits(10000000)
key = generate_secure_key()
byte = open("flag.enc", "rb").read()
file = open("file.pdf", "wb").write(xor(byte,key))