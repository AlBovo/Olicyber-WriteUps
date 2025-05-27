from bs4 import BeautifulSoup
import requests
site = requests.get("http://web-13.challs.olicyber.it/").text # ottengo l'html del sito
zuppetta = BeautifulSoup(site, "html.parser")
print("flag{", end="") # inizio a scrivere la flag
for i in zuppetta.find_all("span"): # ottengo ogni carattere della flag (hanno il tag span)
    print(str(i).replace('<span class="red">', "").replace("</span>",""), end="") # scrivo ogni carattere della flag
print("}") # fine della flag
