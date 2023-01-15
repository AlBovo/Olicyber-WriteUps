import requests
r = requests.head("http://headache.challs.olicyber.it/")
print(r.headers['Flag'])