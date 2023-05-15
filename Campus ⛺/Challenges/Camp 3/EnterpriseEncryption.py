from Crypto.Util.number import *
enc = bytes.fromhex("7971737c7e6d7866646f2c28712e7c2f2f717b402e2b7177292b40772e402a73402f71732f402867407b2c62")
f = b""
for i in range(0, len(enc), 2):
    f += long_to_bytes(enc[i] ^ 31)
for i in range(1, len(enc), 2):
    f += long_to_bytes(enc[i] ^ 31)
print(f.decode(), end="")