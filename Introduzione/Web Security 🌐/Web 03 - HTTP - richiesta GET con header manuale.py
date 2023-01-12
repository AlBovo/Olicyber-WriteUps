import requests
site = "http://web-03.challs.olicyber.it/flag"
req = requests.get(site, headers={"X-Password":"admin"}) # setto gli headers
print(req.text) # printo la flag
