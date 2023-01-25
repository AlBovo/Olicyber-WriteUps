import itertools
def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

f = b"flag{"
t = b""
flag = bytes.fromhex("27893459dc8772d66261ff8633ba1e5097c10fba257293872fd2664690e975d2015fc4fd3c")
for r in range(len(f)):
    for i in itertools.product(["0","1"], repeat=8):
        s = ""
        for e in i:
            s += e
        s = int(s, 2).to_bytes(len(s) // 8, byteorder='big')
        if xor(flag, s*(len(flag)//len(s)+1))[r] == f[r]:
            t += s
for i in itertools.product(["0","1"], repeat=8):
    s = ""
    for e in i:
        s += e
    s = int(s, 2).to_bytes(len(s) // 8, byteorder='big')
    print(xor(flag, (t+s)*(len(flag)//len(t+s)+1))) # contiene Kn0wN
        