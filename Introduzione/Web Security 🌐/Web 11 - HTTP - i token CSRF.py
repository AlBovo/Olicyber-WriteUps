import requests, json
siteLogin = "http://web-11.challs.olicyber.it/login"
siteFlag = "http://web-11.challs.olicyber.it/flag_piece?index="
req = requests.session()
csrf = json.loads(req.post(siteLogin, json={"username":"admin", "password":"admin"}).text)["csrf"] # eseguo il login ottenendo i cookie di sessione
for i in range(4): # ottengo i 4 pezzi della flag
    s = json.loads(req.get(siteFlag + str(i) + "&csrf="+ csrf).text) # mando la richiesta con il token e l'indice
    csrf = s["csrf"] # mi salvo il token
    print(s["flag_piece"], end="") # printo il pezzo della flag