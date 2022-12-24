import requests
site = "http://web-10.challs.olicyber.it/"
req = requests.options(site) # vedo i metodi accettati
print(req.headers["Allow"]) # il metodo put non è accettato
req = requests.put(site) # uso il metodo put
print(req.headers["X-Flag"]) # printo la flag presente negli headers