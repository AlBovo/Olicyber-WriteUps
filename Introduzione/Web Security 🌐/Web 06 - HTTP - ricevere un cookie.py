import requests
siteToken = "http://web-06.challs.olicyber.it/token"
siteFlag = "http://web-06.challs.olicyber.it/flag"
req = requests.session() # sessione avviata
req.get(siteToken) # ottengo i cookie di sessione
print(req.get(siteFlag).text) # ottengo la flag e la printo
