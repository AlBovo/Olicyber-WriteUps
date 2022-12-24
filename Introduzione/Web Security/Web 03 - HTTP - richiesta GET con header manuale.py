import requests
site = "http://web-03.challs.olicyber.it/flag"
req = requests.get(site, headers={"X-Password":"admin"}) # setto gli headers
print(req.text) # printo la flag
''' La flag di questa chall è: flag{7ru57_m3_i_m_7h3_4dmin} '''