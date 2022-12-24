import requests
site = "http://web-07.challs.olicyber.it/"
req = requests.head(site) # Richiedo gli headers del sito
print(req.headers['X-Flag']) # Printo la flag (gli headers sono dei json)
''' La flag di questa chall è: flag{r0gu3_m374d474} '''