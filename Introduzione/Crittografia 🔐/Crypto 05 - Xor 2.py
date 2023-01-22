def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

c = bytes.fromhex("104e137f425954137f74107f525511457f5468134d7f146c4c")
for i in "abcdefghijklmnopqrstuvwxyz0123456789":
    s = b""
    for r in range(len(c)):
        s += i.encode()
    x = xor(c, s).decode()
    print(x)