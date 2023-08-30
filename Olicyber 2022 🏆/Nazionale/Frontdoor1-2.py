#!/usr/bin/env python3 
from flask import Flask, Response, request
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import md5
from z3 import *

secret = [87, 71, 179, 169, 154, 69, 91, 217, 185, 174, 69, 44, 63, 223, 237, 47, 20, 62, 215, 47, 3, 89, 54, 255, 80, 239, 181, 130, 78, 57, 186, 91]
app = Flask(__name__)


@app.route('/')
def main():
    generated = request.headers["User-Agent"].strip().encode()
    print(generated)
    assert len(generated) == 32
    r = Response()
    r.headers['Server-Type'] = 'Frontdoor-Server-1.0'

    risp = [BitVec(f'risp{i}', 8) for i in range(32)]
    s = Solver()
    
    for i in range(31):
        s.add(((risp[i] ^ generated[i]) + (risp[i+1] ^ generated[i+1])) % 256 == secret[i])
    
    if s.check() != sat:
        print("Nope")
        return "Nope", 500
    f = b''
    m = s.model()
    for i in range(32):
        f += bytes([m[risp[i]].as_long()])
    
    r.headers['C&C'] = b64encode(f).decode()
    r.status = 200
    return r

@app.route('/command.txt')
def command():
    print(request.headers["Flag"])
    return "rfile;superhiddensecret.txt", 200

def decrypt(data, plain):
    plainText = b64decode(data)
    md5_hash = md5(plain.encode()).digest()[:-1] + md5(plain.encode()).digest() + b'\x00'
    assert len(md5_hash) == 32
    aes = AES.new(md5_hash, AES.MODE_ECB)
    ret = aes.decrypt(plainText)
    print(ret)
    return

@app.route('/result', methods=['POST'])
def result():
    print(request.data)
    decrypt(request.data, "nothingyoushouldcareabout")
    return "Ok", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)