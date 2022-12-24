from bs4 import BeautifulSoup
import requests
site = requests.get("http://web-14.challs.olicyber.it/").text # ottengo l'html del stio
zuppetta = BeautifulSoup(site, "html.parser")
for flag in str(zuppetta.find_all("head")).split("\n"): # divido il tag head in righe
    if "flag" in str(flag): # seleziono la riga in cui c'è la flag
        print(flag) # printo la riga della flag
''' La flag di questa chall è: flag{50m3b0dy_f0rg07_70_d31373_7hi5} '''