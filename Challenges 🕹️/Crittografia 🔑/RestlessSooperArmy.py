from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util.Padding import unpad

p = 20901558209304821827 # valori usati 
q = 19266041191182381619 # letti usando netcat
e = 65537
r = RSA.construct([p*q,e])
print(r.n)
print((p-1)*(q-1))
d = pow(e, -1, (p-1)*(q-1))
print(d)
r = bytes_to_long(b"CTF")
print(pow(r, e, p*q))
chiave = pow(bytes_to_long(bytes.fromhex("ea69185e01f77cd08d6236de17d85639")), d, p*q)
a = AES.new(long_to_bytes(chiave), AES.MODE_CBC, iv=bytes.fromhex("a1530168843c2e3e46aec4b11b29a4cd"))
print(unpad(a.decrypt(bytes.fromhex("5d8eabe7dc10af7f787e32f003ce7fe6b917fca1562c29ff3b9f27c9622e902d")), AES.block_size))

