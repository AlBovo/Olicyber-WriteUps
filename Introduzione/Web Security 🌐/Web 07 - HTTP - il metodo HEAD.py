import requests
site = "http://web-07.challs.olicyber.it/"
req = requests.head(site) # Richiedo gli headers del sito
print(req.headers['X-Flag']) # Printo la flag (gli headers sono dei json)
