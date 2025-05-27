from Crypto.Cipher import DES, AES, ChaCha20
from Crypto.Util.Padding import *
from Crypto import Random

plain = "La lunghezza di questa frase non è divisibile per 8".encode("utf-8") # da cambiare
cipher = DES.new(bytes.fromhex("91b4aff5ac024f12"), DES.MODE_CBC) # da cambiare
r = cipher.iv
f = cipher.encrypt(pad(plain, 8, "x923"))
print(f.hex())
print(r.hex())

s = Random.get_random_bytes(32)
print(s.hex())
plain = b'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
cipher = AES.new(s, AES.MODE_CFB, segment_size=24)
f = cipher.encrypt(pad(plain, 16, "pkcs7"))
print(cipher.iv.hex())
print(f.hex())

key = bytes.fromhex("621ea04cff7d23bdddcac6e048822511969731da506db416f251eb674b516928")
cipher = bytes.fromhex("d1fe1a59e365c5d2b2ae105500fd0867dc25eb644dbdc34fe365688d")
nonce = bytes.fromhex("a118a4e91b89b269")
s = ChaCha20.new(key=key, nonce=nonce)
print(s.decrypt(cipher).decode())