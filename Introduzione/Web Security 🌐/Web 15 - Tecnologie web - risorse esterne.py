from bs4 import BeautifulSoup
import requests
url = "http://web-15.challs.olicyber.it"
site = requests.get(url).text # ottengo l'html del sito
zuppetta = BeautifulSoup(site, "html.parser")
for file in zuppetta.find_all("link", href=True): # ottengo i link dei css esterni
    css = requests.get(url+file['href']).text # ottengo il codice css
    if "flag" in css: # se c'è la flag la stampo
        print(css)
for file in zuppetta.find_all("script", src=True): # ottengo i link dei js esterni
    js = requests.get(url+file['src']).text # ottengo il codice js
    if "flag" in js: # se c'è la flag la stampo
        print(js)
