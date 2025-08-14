#!/usr/bin/env python3
import argparse
from pathlib import Path
import numpy as np
from PIL import Image
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

WHITE = np.array([255, 255, 255, 255], dtype=np.uint8)

def read_marker_color(path):
    with Image.open(path).convert("RGBA") as im:
        n = np.array(im, dtype=np.uint8)
    mask = (n[:, :, 0:4] != WHITE).any(axis=2)
    y, x = np.argwhere(mask)[0]
    return n[y, x, 0:4].astype(np.uint8)

g = read_marker_color("g.png")
A = read_marker_color("A.png")
B = read_marker_color("B.png")

shared = (A.astype(np.int16) + B.astype(np.int16) - g.astype(np.int16)) % 256
shared_bytes = bytes(shared.astype(np.uint8).tolist())  # 4 byte

key = sha256(shared_bytes).digest()

ct_hex = open("ciphertext.txt").read().strip()
ct = bytes.fromhex(ct_hex)
iv, c = ct[:16], ct[16:]

cipher = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(c), 16)

print(pt.decode())