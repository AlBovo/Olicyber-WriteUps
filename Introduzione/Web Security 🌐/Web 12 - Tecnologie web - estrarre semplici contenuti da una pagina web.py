from bs4 import BeautifulSoup
import requests
site = requests.get("http://web-12.challs.olicyber.it/").text # ottengo l'html del sito
zuppetta = BeautifulSoup(site, "html.parser")
for flag in zuppetta.find_all("pre"): # cerco per i tag <pre>
    print(str(flag).replace("<pre>","").replace("</pre>","")) # printo tutti i tag pre (l'unico è quello della flag)
