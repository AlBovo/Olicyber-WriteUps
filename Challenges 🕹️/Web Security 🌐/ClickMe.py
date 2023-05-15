from bs4 import BeautifulSoup
import requests
site = "http://click-me.challs.olicyber.it/"
s = requests.Session()
f = s.get(site, cookies={"cookies":f"{10000000}"}).text
b = BeautifulSoup(f, 'html.parser')
for i in b.find_all("h1"):
    print(str(i).replace("<h1>","").replace("</h1>",""), end="")