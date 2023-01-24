import itertools
def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

c = bytes.fromhex("104e137f425954137f74107f525511457f5468134d7f146c4c")
for i in itertools.product([0, 1], repeat=8):
    temp = ""
    for e in i:
        temp += str(e)
    b = bitstring_to_bytes(temp)
    print(xor(b*len(c), c))
    # la flag è 0n3_byt3_T0_ru1e_tH3m_4Ll => flag{0n3_byt3_T0_ru1e_tH3m_4Ll}