import requests, json
site = "http://flagdownloader.challs.olicyber.it/download/flag/"
i = "0"
while True:
    r = requests.get(site + i)
    f = json.loads(r.text)
    print(f["c"], end="")
    i = f["n"]
    if f["c"] == "}":
        exit(0)