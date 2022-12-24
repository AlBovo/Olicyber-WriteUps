import requests
site = "http://web-04.challs.olicyber.it/users"
req = requests.get(site, headers={"Accept":"application/xml"}) # sempre la richiesta
print(req.text) # printo la richiesta con la flag
''' La flag di questa chall è: flag{54m3_7hing_diff3r3n7_7hing} '''