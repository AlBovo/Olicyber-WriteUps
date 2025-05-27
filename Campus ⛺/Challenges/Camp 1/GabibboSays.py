#!/usr/bin/env python3
import requests, re

SITE = "http://gabibbo-says.challs.olicyber.it/"
REGEX = r"flag{.*?}"

r = requests.post(SITE, data={"gabibbo":"angry"})
flag = re.findall(REGEX, r.text)[0]
print(flag)