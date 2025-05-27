#!/usr/bin/env python3
from datetime import datetime
import requests, random, string, hashlib, hmac, time

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def sign(text, key):
    textAsBytes = bytes(text, encoding='ascii')
    keyAsBytes  = bytes(key, encoding='ascii')
    signature = hmac.new(keyAsBytes, textAsBytes, hashlib.sha256)
    return signature.hexdigest()

def verify(text, signature, key):
    expected_signature = sign(text, key)
    print(expected_signature, signature)
    return hmac.compare_digest(expected_signature, signature)

seed = int(time.time())
site = "http://trulyrandomsignature.challs.olicyber.it/"
r = requests.get(site)
print(r.headers["X-Uptime"])
l = time.localtime(seed - int(r.headers["X-Uptime"]))
t, c = l.tm_sec, l.tm_min
if t < 10:
    t = "0" + str(l.tm_sec)
if c < 10:
    c = "0" + str(l.tm_min)
f = f"{l.tm_year}-0{l.tm_mon}-0{l.tm_mday} {l.tm_hour}-{c}-{t}"
print(f)
random.seed(f)
SUPER_SECRET_KEY = get_random_string(32)
print(SUPER_SECRET_KEY)
if verify(r.cookies.get_dict()["user"], r.cookies.get_dict()["signature"], SUPER_SECRET_KEY):
    print("hey")
