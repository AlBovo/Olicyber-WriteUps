import requests
site = "http://web-08.challs.olicyber.it/login"
dat = [["username", "admin"], ["password", "admin"]] # creo il dizionario (simile ad un json o una map in c++)
req = requests.post(site, data=dat) # Mando la richiesta al sito
print(req.text) # Printo la flag
''' La flag di questa chall è: flag{53nding_d474_7h3_01d_w4y} '''