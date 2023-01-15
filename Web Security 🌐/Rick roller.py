import requests
r = requests.get("http://roller.challs.olicyber.it/get_flag.php")
print(r.text.encode())