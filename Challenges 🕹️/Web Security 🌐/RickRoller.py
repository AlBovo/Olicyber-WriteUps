import requests
r = requests.get("http://roller.challs.olicyber.it/get_flag.php", allow_redirects=False)
print(r.text, end="")