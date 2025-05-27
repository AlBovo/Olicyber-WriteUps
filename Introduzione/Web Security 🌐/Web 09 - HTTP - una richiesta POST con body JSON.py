import requests, json # uso pure la libreria json per trasformare un json in un dizionario
site = "http://web-09.challs.olicyber.it/login"
req = requests.post(site, json={"username":"admin","password":"admin"}) # mando la flag
print(json.loads(req.text)["token"]) # printo la flag (la richiesta restituisce un json)