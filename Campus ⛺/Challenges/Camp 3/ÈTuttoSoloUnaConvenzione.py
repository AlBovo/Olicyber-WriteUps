import requests
r = requests.request(method="FLAG", url="http://convenzione.challs.olicyber.it/")
for i in r.headers:
    if "flag" in r.headers[i]:
        print(r.headers[i], end="")