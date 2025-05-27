# estraendo l'elf dal file wireshark possiamo reversarlo e trovare la flag
def xor(a, b): # template di xor (c'è sul sito di olicyber)
    return bytes([x^y for x,y in zip(a,b)])

v1 = "6975797472657771"
v2 = "19184937090b1410"
print(xor(bytes.fromhex(v1), bytes.fromhex(v2)).decode()) # spero sia quella giusta lol non l'hanno detta quella giusta