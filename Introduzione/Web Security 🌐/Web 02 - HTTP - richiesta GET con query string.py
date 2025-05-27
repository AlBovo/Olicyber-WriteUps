import requests
req = requests.get("http://web-02.challs.olicyber.it/server-records", params="id=flag") # eseguo una richiesta del tipo url.it/?id=flag
print(req.text) # scrivo su console la flag
