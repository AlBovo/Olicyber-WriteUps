import codecs
flag = open("chall.png", "rb").read()
res = open("flag.png", "wb")
f = b""
number = codecs.decode(bytearray("89504E470D0A1A0A",encoding="utf-8"), "hex")
f += number + flag[8:]
res.write(f) # la flag è in flag.png