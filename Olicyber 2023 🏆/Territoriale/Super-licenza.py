from Crypto.Util.number import *
def riordina(data):
    data1 = b""
    v3 = [0]*52
    v3[13] = 0
    v3[25] = 1
    v3[31] = 2
    v3[10] = 3
    v3[11] = 4
    v3[15] = 5
    v3[44] = 6
    v3[51] = 7
    v3[4] = 8
    v3[46] = 9
    v3[19] = 10
    v3[28] = 11
    v3[22] = 12
    v3[50] = 13
    v3[9] = 14
    v3[30] = 15
    v3[18] = 16
    v3[20] = 17
    v3[0] = 18
    v3[26] = 19
    v3[45] = 20
    v3[42] = 21
    v3[6] = 22
    v3[48] = 23
    v3[2] = 24
    v3[39] = 25
    v3[16] = 26
    v3[7] = 27
    v3[8] = 28
    v3[24] = 29
    v3[34] = 30
    v3[17] = 31
    v3[37] = 32
    v3[36] = 33
    v3[14] = 34
    v3[3] = 35
    v3[41] = 36
    v3[33] = 37
    v3[12] = 38
    v3[23] = 39
    v3[1] = 40
    v3[40] = 41
    v3[35] = 42
    v3[49] = 43
    v3[27] = 44
    v3[21] = 45
    v3[29] = 46
    v3[43] = 47
    v3[32] = 48
    v3[47] = 49
    v3[5] = 50
    v3[38] = 51
    for i in range(52):
        data1 += long_to_bytes(data[v3[i]])
    return data1
    
def xorare(data):
    data1 = b""
    mat = bytearray.fromhex("9A F8 1F 2B 1B E0 AB 1F  C3 62 FE DA A8 3F 70 3C 75 19 30 A0 48 C1 54 CA 75 E6 75 A6 DE 16 6E EF 18 ED E6 FC E4 11 06 A3 AF 5E 1D 24 F6 5D CA 8E A3 EA 96 A5".replace(" ", "").lower())
    for i in range(52):
        data1 += long_to_bytes(data[i] ^ mat[i])
    return data1
data = bytearray.fromhex("AA A7 7D 74 69 81 92 62  B8 07 CF A8 9C 07 11 63 17 77 56 D8 79 F1 21 AC 14 82 2A 96 AA 73 59 9C 29 DA 92 9B D0 70 73 FC C3 3F 78 40 C6 33 FE EF 95 DE E4 C7".replace(" ", "").lower())
print(len(data))
data = xorare(data)
data = riordina(data)
print(data)