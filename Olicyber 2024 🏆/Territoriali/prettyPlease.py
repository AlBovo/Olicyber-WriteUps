#!/usr/bin/env python3
import requests, re
URL = 'http://prettyplease.challs.olicyber.it/'
REGEX = r'flag{.*}'

r = requests.post(URL, data={'how' : 'pretty please'})
print(re.findall(REGEX, r.text)[0])
