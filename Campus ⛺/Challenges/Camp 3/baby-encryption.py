b = bytes.fromhex("2b53f86f8683c39c8b35f0c087922e41")
b1 = bytes.fromhex("272d20263a3629702d72701e3971333c")
v = b""
def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

def rotate_key(k):
    return k[len(k)-1:]+k[:len(k)-1]
    
for i in range(16):
    b1 = xor(b, b1) 
    b = rotate_key(b)
print(b1)
