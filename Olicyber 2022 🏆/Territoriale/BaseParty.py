import base64
flag = open("encoded.txt", "rb").read()
for i in range(5):
    flag = bytes.fromhex(flag.decode())
    flag = base64.b32decode(flag)
    flag = base64.b64decode(flag)
print(flag.decode())