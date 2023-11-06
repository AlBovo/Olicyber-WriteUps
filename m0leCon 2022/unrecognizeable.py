#!/usr/bin/env python3
from PIL import Image

image = Image.open("whoami.png")
chall = Image.open("challenge.png")
result = Image.new("RGB", image.size)

assert chall.size == image.size
xImage, yImage = image.size

for i in range(xImage):
    for e in range(yImage):
        f0 = image.getpixel((i, e))
        f1 = chall.getpixel((i, e))
        r1 = (f0[0] ^ f1[0], f0[1] ^ f1[1], f0[2] ^ f1[2])
        result.putpixel((i, e), r1)

result.save("result.png")