import requests
site = "http://web-04.challs.olicyber.it/users"
req = requests.get(site, headers={"Accept":"application/xml"}) # sempre la richiesta
print(req.text) # printo la richiesta con la flag
