import requests
site = "http://web-05.challs.olicyber.it/flag"
req = requests.get(site, cookies={"password":"admin"}) # richiesta con cookie
print(req.text) # printo la richiesta (flag)
