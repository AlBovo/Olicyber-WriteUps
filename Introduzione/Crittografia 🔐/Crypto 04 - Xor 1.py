def xor(a, b): # template di xor (c'è sul sito di olicyber)
    return bytes([x^y for x,y in zip(a,b)])

flag1 = bytes.fromhex("158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf") # prima parte della flag
flag2 = bytes.fromhex("73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2") # seconda parte della flag
print(xor(flag1, flag2).decode("ascii")) # decripto la flag e la printo
