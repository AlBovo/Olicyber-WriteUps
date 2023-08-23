#!/usr/bin/env python3
from urllib.parse import quote
import requests

SITE = "http://treasure.challs.olicyber.it/flag?password="
PAYLOAD = quote("Belandi, dammi la flag!") # trovata nel tag script dell'index.html

r = requests.get(SITE + PAYLOAD)
print(r.text)